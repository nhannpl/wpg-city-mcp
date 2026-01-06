import httpx
import config
from tools import locations, routing

async def plan_trip(origin: str, destination: str, mode: str = "depart-after") -> str:
    """
    Plan a trip between two points using Winnipeg Transit.
    
    Arguments 'origin' and 'destination' can be:
    - Plain text addresses or landmarks (e.g. "The Forks", "IKEA", "123 Main St") - Resolved via OSM
    - Stop numbers (e.g. "10625", "Stop 10541")
    - Formatted keys:
        - "stops/{key}"
        - "geo/{lat},{lon}"
        - "intersection/{key}"
    """
    formatted_origin = await locations.format_location(origin)
    formatted_dest = await locations.format_location(destination)
    
    if not locations.is_valid_format(formatted_origin):
        return f"Error: Could not find/resolve origin: '{origin}'."
    if not locations.is_valid_format(formatted_dest):
        return f"Error: Could not find/resolve destination: '{destination}'."

    url = config.TRANSIT_TRIP_PLANNER_URL
    params = {
        "api-key": config.TRANSIT_API_KEY,
        "origin": formatted_origin,
        "destination": formatted_dest,
        "mode": mode or "depart-after"
    }
    
    try:
        headers = {"User-Agent": "WinnipegTransitMCP/1.0"}
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
                start_seg = seg_times.get("start", "").split("T")[-1][:-3]
                end_seg = seg_times.get("end", "").split("T")[-1][:-3]
                
                if type_ == "walk":
                    w_time = seg_durations.get("walking", 0)
                    
                    # Extract destination info
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
                    
                    # Internal helper for coordinates dict extraction
                    def get_location_coords_dict(node):
                        entities = []
                        for key in ['stop', 'intersection', 'monument', 'point']:
                            if key in node: entities.append(node[key])
                        for key in ['origin', 'destination']:
                            if key in node:
                                inner = node[key]
                                for subkey in ['point', 'stop', 'intersection', 'monument']:
                                    if subkey in inner: entities.append(inner[subkey])
                        for entity in entities:
                            if "centre" in entity and "geographic" in entity["centre"]:
                                return entity["centre"]["geographic"]
                        return None

                    from_geo = get_location_coords_dict(seg.get("from", {}))
                    to_geo = get_location_coords_dict(seg.get("to", {}))

                    if from_geo and to_geo:
                        f_lat, f_lon = from_geo.get("latitude"), from_geo.get("longitude")
                        t_lat, t_lon = to_geo.get("latitude"), to_geo.get("longitude")
                        
                        steps = await routing.get_walking_directions(f_lat, f_lon, t_lat, t_lon)
                        if steps:
                            result.extend(steps)
                        
                        map_url = f"https://www.google.com/maps/dir/?api=1&origin={f_lat},{f_lon}&destination={t_lat},{t_lon}&travelmode=walking"
                        result.append(f"     🗺️ Map: {map_url}")
                    
                elif type_ == "ride":
                    r_time = seg_durations.get("riding", 0)
                    route = seg.get("route", {})
                    r_name = route.get("name", "Bus")
                    r_num = route.get("key", "")
                    variant = seg.get("variant", {}).get("name", "")
                    
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
            
    except Exception as e:
        return f"Error executing plan_trip: {str(e)}"

async def plan_journey(stops: list[str], optimize: bool = False) -> str:
    """
    Plan a multi-stop journey (A -> B -> C ...).
    
    Args:
        stops: List of locations (plain text, stop numbers, or formatted keys)
        optimize: If True, optimized the visit order (TSP) starting from the first stop.
    """
    if len(stops) < 2:
        return "Error: Need at least 2 stops to plan a journey."
    
    # 1. Format/Resolve all stops first
    # We maintain a map of Resolved -> Original Name for display purposes
    resolved_map = {} # formatted -> original
    formatted_stops = []
    
    for s in stops:
        fmt = await locations.format_location(s)
        formatted_stops.append(fmt)
        if fmt not in resolved_map:
            resolved_map[fmt] = s
            
    # 2. Optimize if requested
    if optimize:
        formatted_stops = await routing.optimize_stop_order_greedy(formatted_stops)
        
    results = []
    if optimize:
        results.append(f"ℹ️ Route Optimization Enabled. New Order: {' -> '.join([resolved_map.get(f, f) for f in formatted_stops])}\n")
    
    for i in range(len(formatted_stops) - 1):
        origin = formatted_stops[i]
        dest = formatted_stops[i+1]
        
        origin_label = resolved_map.get(origin, origin)
        dest_label = resolved_map.get(dest, dest)
        
        # We perform the plan. Note: plan_trip will re-format, but it's idempotent.
        leg_result = await plan_trip(origin, dest)
        results.append(f"--- Leg {i+1}: {origin_label} to {dest_label} ---\n{leg_result}")
        
    return "\n\n".join(results)
