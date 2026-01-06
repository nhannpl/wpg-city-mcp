import httpx
import asyncio
import os

TRANSIT_API_KEY = os.getenv("TRANSIT_API_KEY")
if not TRANSIT_API_KEY:
    # Try to load from .env if available, useful for local testing
    try:
        from dotenv import load_dotenv
        load_dotenv()
        TRANSIT_API_KEY = os.getenv("TRANSIT_API_KEY")
    except ImportError:
        pass

if not TRANSIT_API_KEY:
    print("Warning: TRANSIT_API_KEY not set in environment")
# URL = f"https://api.winnipegtransit.com/v4/stops.json?api-key={TRANSIT_API_KEY}&name=Portage"
# URL = f"https://api.winnipegtransit.com/v4/locations.json?api-key={TRANSIT_API_KEY}&name=Portage"
# URL = f"https://api.winnipegtransit.com/v4/stops/10625/schedule.json?api-key={TRANSIT_API_KEY}"
# URL = f"https://api.winnipegtransit.com/v4/stops.json?api-key={TRANSIT_API_KEY}&lat=49.8951&lon=-97.1384&distance=200"
URL = f"https://api.winnipegtransit.com/v4/locations.json?api-key={TRANSIT_API_KEY}&name=Portage"

async def test():
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    async with httpx.AsyncClient(headers=headers) as client:
        resp = await client.get(URL)
        print(f"Status: {resp.status_code}")
        try:
            data = resp.json()
            print(f"Count: {len(data.get('stops', []))}")
            if data.get('stops'):
                print(f"First result: {data['stops'][0]['name']}")
        except:
            print(f"Body: {resp.text[:200]}")

asyncio.run(test())
