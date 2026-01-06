import httpx
import config

# --- Constants ---

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

VALID_PREFIXES = ("stops/", "geo/", "intersection/", "addresses/", "monuments/")

# --- Core Functions ---

async def resolve_address_osm(query: str) -> str | None:
    """Resolve a free-text address to geo coordinates using OSM."""
    try:
        headers = {"User-Agent": "WinnipegTransitMCP/1.0"}
        search_url = "https://nominatim.openstreetmap.org/search"
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

async def format_location(loc: str) -> str:
    """Format a user input location into a Transit API compatible string."""
    loc = loc.strip()
    
    # 1. Hardcoded landmarks map
    if loc.lower() in LANDMARKS:
        return LANDMARKS[loc.lower()]

    # 2. Known Formats check
    if loc.isdigit():
        return f"stops/{loc}"
    if loc.lower().startswith("stop "):
        parts = loc.split()
        if len(parts) > 1 and parts[1].isdigit():
            return f"stops/{parts[1]}"
    
    # If already formatted, return as is
    if "/" in loc:
        return loc
        
    # 3. Dynamic Resolution (OSM)
    resolved = await resolve_address_osm(loc)
    if resolved:
        return resolved

    # 4. Fallback
    return loc

def is_valid_format(loc: str) -> bool:
    """Check if a location string appears to be a valid, resolved Transit API format."""
    if loc.isdigit(): return True
    for prefix in VALID_PREFIXES:
        if loc.startswith(prefix): return True
    return False

async def get_coordinates(loc_formatted: str) -> tuple[float, float] | None:
    """
    Extract or fetch coordinates for a formatted location string.
    Returns (lat, lon) or None.
    """
    try:
        if loc_formatted.startswith("geo/"):
            parts = loc_formatted[4:].split(",")
            return float(parts[0]), float(parts[1])
            
        if loc_formatted.startswith("stops/"):
            stop_key = loc_formatted.split("/")[1]
            url = f"{config.TRANSIT_BASE_URL}/stops/{stop_key}.json"
            params = {"api-key": config.TRANSIT_API_KEY}
            async with httpx.AsyncClient() as client:
                resp = await client.get(url, params=params)
                if resp.status_code == 200:
                    stop = resp.json().get("stop", {})
                    geo = stop.get("centre", {}).get("geographic", {})
                    if "latitude" in geo and "longitude" in geo:
                        return float(geo["latitude"]), float(geo["longitude"])
    except Exception as e:
        print(f"Error fetching coords for {loc_formatted}: {e}")
    return None
