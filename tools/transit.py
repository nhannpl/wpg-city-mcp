import httpx
import asyncio
import urllib.parse
import config

async def get_bus_arrivals(stop_number: int) -> str:
    """Get real-time bus arrivals for a specific Winnipeg Transit stop number."""
    url = config.TRANSIT_STOP_SCHEDULE_URL.format(stop_number=stop_number, api_key=config.TRANSIT_API_KEY)
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        
        # Extract the next 3 buses
        schedules = data.get("stop-schedule", {}).get("route-schedules", [])
        results = []
        for route in schedules:
            route_name = route['route']['name']
            for arrival in route['scheduled-stops'][:2]:
                # API v4: times -> arrival -> estimated
                time = arrival['times']['arrival']['estimated']
                results.append(f"Route {route_name}: Arriving at {time}")
        
        return "\n".join(results) if results else "No upcoming buses found."

async def get_commute_status(stop_number: int) -> str:
    """
    Smart Commute: Get bus arrivals combined with current weather conditions.
    Helpful for deciding if you need a parka or just a light jacket while waiting.
    """
    transit_url = config.TRANSIT_STOP_SCHEDULE_URL.format(stop_number=stop_number, api_key=config.TRANSIT_API_KEY)
    
    weather_params = {
        "latitude": config.WINNIPEG_LAT,
        "longitude": config.WINNIPEG_LON,
        "current": "temperature_2m,apparent_temperature,wind_speed_10m"
    }

    async with httpx.AsyncClient() as client:
        # RESUME TIP: This demonstrates 'Async Orchestration'. 
        # We fetch both datasources in parallel to minimize user latency.
        transit_resp, weather_resp = await asyncio.gather(
            client.get(transit_url),
            client.get(config.WEATHER_API_URL, params=weather_params)
        )
        
        # Process Weather
        weather_summary = "Weather currently unavailable."
        if weather_resp.status_code == 200:
            w_data = weather_resp.json().get('current', {})
            temp = w_data.get('temperature_2m')
            feels_like = w_data.get('apparent_temperature')
            wind = w_data.get('wind_speed_10m')
            weather_summary = f"{temp}°C (Feels like {feels_like}°C) with {wind}km/h winds."

        # Process Transit (Reuse logic)
        transit_summary = "No buses found."
        if transit_resp.status_code == 200:
            t_data = transit_resp.json()
            schedules = t_data.get("stop-schedule", {}).get("route-schedules", [])
            results = []
            for route in schedules:
                route_name = route['route']['name']
                # Get first bus only for brevity in this combined view
                if route.get('scheduled-stops'):
                    next_bus = route['scheduled-stops'][0]
                    time = next_bus['times']['arrival']['estimated']
                    results.append(f"Route {route_name}: {time}")
            if results:
                transit_summary = "Upcoming Buses:\n" + "\n".join(results)

    return f"""
--- 🚌 COMMUTE REPORT ---
🌡️ Conditions: {weather_summary}
-------------------------
{transit_summary}
"""

async def find_stops_near(lat: float, lon: float, distance_meters: int = 500) -> str:
    """
    Search for bus stops near a specific geographic coordinate.
    Useful when you know the location (e.g. from a user's known lat/lon) but need stop IDs.
    
    NOTE: Distance is capped at 2000 meters to allow efficient querying.
    """
    # API tends to 500 Error if distance is too large (e.g. 50km)
    safe_distance = min(distance_meters, 2000)
    
    url = config.TRANSIT_STOPS_SEARCH_URL.format(lat=lat, lon=lon, distance=safe_distance, api_key=config.TRANSIT_API_KEY)

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        
        if response.status_code != 200:
            return f"Error searching for stops: {response.status_code}"
            
        data = response.json()
        stops = data.get('stops', [])
        
        if not stops:
            return f"No stops found within {distance_meters}m of {lat}, {lon}."
            
        results = []
        for stop in stops[:10]: # Limit to 10 results
            stop_name = stop.get('name', 'Unknown')
            stop_num = stop.get('number', stop.get('key', '00000'))
            direction = stop.get('direction', '')
            results.append(f"- {stop_name} ({direction}) -> Stop #{stop_num}")
            
        return f"Bus stops near {lat}, {lon}:\n" + "\n".join(results)
