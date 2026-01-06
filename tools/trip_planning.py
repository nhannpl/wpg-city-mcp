import httpx
import config

async def plan_trip(origin: str, destination: str, mode: str = "depart-after") -> str:
    """
    Plan a trip between two points using Winnipeg Transit.
    
    IMPORTANT: The 'origin' and 'destination' arguments must be formatted strings, not free-text addresses.
    
    Formats:
    - Stops: "stops/{stop_key}" (e.g. "stops/10625") or just "10625"
    - Coordinates: "geo/{lat},{lon}" (e.g. "geo/49.8951,-97.1384")
    - Intersections: "intersection/{key}" (if key is known)
    - Addresses: "address/{key}" (if key is known)
    
    Note: Automatic address resolution (looking up keys from names) is currently unavailable.
    """
    url = config.TRANSIT_TRIP_PLANNER_URL

    # Helper to resolve address using OSM Nominatim
    async def resolve_address_osm(query: str) -> str | None:
        try:
            # Simple header to identify our app (required by Nominatim terms)
            headers = {"User-Agent": "WinnipegTransitMCP/1.0"}
            search_url = "https://nominatim.openstreetmap.org/search"
            # biasing towards Winnipeg
            params = {
                "q": f"{query}, Winnipeg, MB",
                "format": "json",
                "limit": 1
            }
            async with httpx.AsyncClient(headers=headers) as client:
                resp = await client.get(search_url, params=params)
                if resp.status_code == 200:
                    data = resp.json()
                    if data:
                        lat = data[0]['lat']
                        lon = data[0]['lon']
                        return f"geo/{lat},{lon}"
        except Exception as e:
            print(f"OSM Resolution failed: {e}")
        return None

    # Helper to format location
    async def format_location(loc: str) -> str:
        loc = loc.strip()
        
        # 1. Hardcoded landmarks map (Fastest fallback)
        LANDMARKS = {
            "polo park": "stops/10541",
            "the forks": "geo/49.8887,-97.1314",
            "portage and main": "stops/10627",
            "u of m": "stops/60160",
            "university of manitoba": "stops/60160",
            "airport": "stops/20006",
            "ywg": "stops/20006",
            "kp": "stops/40149",
            "kildonan place": "stops/40149",
            "st vital mall": "stops/50454"
        }
        
        if loc.lower() in LANDMARKS:
            return LANDMARKS[loc.lower()]

        # 2. Known Formats check
        # If it looks like a stop number (digits), format as stop key
        if loc.isdigit():
            return f"stops/{loc}"
        # If it starts with "stop " (case insensitive), format as stop key
        if loc.lower().startswith("stop "):
            parts = loc.split()
            if len(parts) > 1 and parts[1].isdigit():
                return f"stops/{parts[1]}"
        # If matches "geo/...", "stops/...", "intersection/..." leave as is
        if "/" in loc:
            return loc
            
        # 3. Dynamic Resolution (OSM)
        # If we are here, it's a free text string like "IKEA" or "123 Main St"
        # Since the official API is down, we use OSM.
        resolved = await resolve_address_osm(loc)
        if resolved:
            return resolved

        # 4. Give up and return as is (let API try valid it or fail)
        return loc

    # Helper to get walking directions from OSRM
    async def get_walking_directions(lat1, lon1, lat2, lon2):
        try:
            # OSRM Public API (Project OSRM)
            # endpoint: /route/v1/walking/{lon1},{lat1};{lon2},{lat2}?steps=true
            osrm_url = f"http://router.project-osrm.org/route/v1/walking/{lon1},{lat1};{lon2},{lat2}"
            params = {"steps": "true", "overview": "false"}
            
            async with httpx.AsyncClient() as client:
                resp = await client.get(osrm_url, params=params)
                if resp.status_code == 200:
                    data = resp.json()
                    routes = data.get("routes", [])
                    if routes:
                        steps = routes[0].get("legs", [])[0].get("steps", [])
                        instructions = []
                        for step in steps:
                            maneuver = step.get("maneuver", {})
                            m_type = maneuver.get("type", "")
                            modifier = maneuver.get("modifier", "")
                            street = step.get("name", "") or "path"
                            
                            # Basic formatting
                            direction = f"{m_type} {modifier}".strip()
                            if m_type == "depart": direction = "Head"
                            if m_type == "arrive": direction = "Arrive"
                            
                            instr = f"{direction} on {street}" if street else direction
                            # Clean up text
                            instr = instr.replace("  ", " ").strip().capitalize()
                            instructions.append(f"       ↳ {instr}")
                            
                        return instructions
        except Exception:
            pass
        return []

    formatted_origin = await format_location(origin)
    formatted_dest = await format_location(destination)

    # Validation to identify which location failed
    # Valid formats from format_location will be stops/, geo/, or landmaks (mapped to stops/geo)
    # The API also technically supports 'intersection/' and 'addresses/' if known keys are used.
    valid_prefixes = ("stops/", "geo/", "intersection/", "addresses/", "monuments/")
    
    # Helper to check if a location string appears "resolved" (valid transit format or simple stop number)
    def is_valid_format(loc: str) -> bool:
        if loc.isdigit(): return True
        # Check prefixes
        for prefix in valid_prefixes:
            if loc.startswith(prefix): return True
        return False

    if not is_valid_format(formatted_origin):
        return f"Error: Could not find/resolve origin: '{origin}'. Try checking the spelling (e.g. '143 Egesz') or using a stop number."
        
    if not is_valid_format(formatted_dest):
        return f"Error: Could not find/resolve destination: '{destination}'. Try checking the spelling or using a stop number."

    params = {
        "api-key": config.TRANSIT_API_KEY,
        "origin": formatted_origin,
        "destination": formatted_dest,
        "mode": mode or "depart-after"
    }
    
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    
    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.get(url, params=params)
        
        if response.status_code != 200:
            return f"Error planning trip: {response.status_code} - {response.text}"
            
        data = response.json()
        plans = data.get("plans", [])
        if not plans:
            return f"No trip plans found from {origin} to {destination}."
            
        # Format the first (best) plan
        plan = plans[0]
        segments = plan.get("segments", [])
        times = plan.get("times", {})
        durations = times.get("durations", {})
        
        start_time = times.get("start", "Unknown").replace("T", " ")
        end_time = times.get("end", "Unknown").replace("T", " ")
        
        total_min = durations.get("total", 0)
        walk_min = durations.get("walking", 0)
        wait_min = durations.get("waiting", 0)
        ride_min = durations.get("riding", 0)
        
        result = [
            f"Trip: {origin} -> {destination}",
            f"Date: {start_time}",
            f"Total Duration: {total_min} min",
            f"  - 🚶 Walking: {walk_min} min",
            f"  - ⏳ Waiting: {wait_min} min",
            f"  - 🚌 Riding: {ride_min} min",
            "------------------------------------------------"
        ]
        
        for seg in segments:
            type_ = seg.get("type", "")
            seg_times = seg.get("times", {})
            seg_durations = seg_times.get("durations", {})
            start_seg = seg_times.get("start", "").split("T")[-1][:-3] # HH:MM
            end_seg = seg_times.get("end", "").split("T")[-1][:-3]
            
            if type_ == "walk":
                w_time = seg_durations.get("walking", 0)
                
                # Extract destination info with stop number if available
                to_obj = seg.get("to", {})
                if "stop" in to_obj:
                    s = to_obj["stop"]
                    to_node = f"{s.get('name', 'Stop')} (#{s.get('key', '')})"
                elif "intersection" in to_obj:
                    to_node = to_obj["intersection"].get("name", "Intersection")
                elif "monument" in to_obj:
                    to_node = to_obj["monument"].get("name", "Landmark")
                else:
                    to_node = "Destination"
                    
                result.append(f"  🚶 Walk to {to_node}")
                result.append(f"     (approx {w_time} mins) • {start_seg} - {end_seg}")
                
                # Add Google Maps link & OSRM instructions
                try:
                    def get_location_coords(node):
                        # Node is likely 'from' or 'to' dictionary
                        # Possible keys: 'stop', 'intersection', 'monument', 'origin', 'destination'
                        
                        entities = []
                        # Direct entities
                        for key in ['stop', 'intersection', 'monument', 'point']:
                            if key in node:
                                entities.append(node[key])
                        
                        # Nested in origin/destination
                        for key in ['origin', 'destination']:
                            if key in node:
                                inner = node[key]
                                for subkey in ['point', 'stop', 'intersection', 'monument']:
                                    if subkey in inner:
                                        entities.append(inner[subkey])
                                        
                        for entity in entities:
                            if "centre" in entity and "geographic" in entity["centre"]:
                                return entity["centre"]["geographic"]
                        return None

                    from_geo = get_location_coords(seg.get("from", {}))
                    to_geo = get_location_coords(seg.get("to", {}))

                    if from_geo and to_geo:
                        f_lat, f_lon = from_geo.get("latitude"), from_geo.get("longitude")
                        t_lat, t_lon = to_geo.get("latitude"), to_geo.get("longitude")
                        
                        # Fetch OSRM Steps
                        steps = await get_walking_directions(f_lat, f_lon, t_lat, t_lon)
                        if steps:
                            result.extend(steps)
                        
                        map_url = f"https://www.google.com/maps/dir/?api=1&origin={f_lat},{f_lon}&destination={t_lat},{t_lon}&travelmode=walking"
                        result.append(f"     🗺️ Map: {map_url}")
                except Exception as e:
                    pass # Keep going if map/instructions fail
                
            elif type_ == "ride":
                r_time = seg_durations.get("riding", 0)
                route = seg.get("route", {})
                r_name = route.get("name", "Bus")
                r_num = route.get("key", "")
                variant = seg.get("variant", {}).get("name", "")
                
                # Extract board/alight stop info
                from_obj = seg.get("from", {})
                to_obj = seg.get("to", {})
                
                board_at = "Unknown Stop"
                if "stop" in from_obj:
                    s = from_obj["stop"]
                    board_at = f"{s.get('name')} (#{s.get('key')})"
                    
                alight_at = "Unknown Stop"
                if "stop" in to_obj:
                    s = to_obj["stop"]
                    alight_at = f"{s.get('name')} (#{s.get('key')})"

                result.append(f"  🚌 Ride {r_num} {r_name} ({variant})")
                result.append(f"     Board at: {board_at}")
                result.append(f"     Get off at: {alight_at}")
                result.append(f"     ({r_time} mins) • {start_seg} - {end_seg}")
                
            elif type_ == "transfer":
                result.append(f"  🔄 Transfer")
                
        return "\n".join(result)

async def plan_journey(stops: list[str]) -> str:
    """
    Plan a multi-stop journey (A -> B -> C ...).
    Provide a list of locations/stops.
    """
    if len(stops) < 2:
        return "Error: Need at least 2 stops to plan a journey."
    
    results = []
    
    # We plan each leg sequentially. 
    # Note: A smarter implementation might use the arrival time of Leg 1 
    # to set the departure time of Leg 2, but for now we default to 'depart now' 
    # or consecutive 'depart after' if we wanted to be fancy (not implemented yet).
    # Real-istically, user wants to know how to get from A to B, then B to C.
    
    for i in range(len(stops) - 1):
        origin = stops[i]
        dest = stops[i+1]
        leg_result = await plan_trip(origin, dest)
        results.append(f"--- Leg {i+1}: {origin} to {dest} ---\n{leg_result}")
        
    return "\n\n".join(results)
