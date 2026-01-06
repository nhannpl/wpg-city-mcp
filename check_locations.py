
import httpx
import asyncio
import os
import config
from dotenv import load_dotenv

load_dotenv()

async def check_locations():
    api_key = os.getenv("TRANSIT_API_KEY")
    print(f"DEBUG: API Key present: {bool(api_key)}")
    if api_key:
        print(f"DEBUG: API Key start: {api_key[:4]}...")
    
    if not api_key:
        print("No API Key")
        return

    queries = ["Polo Park", "Portage and Main"]
    
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    
    async with httpx.AsyncClient(headers=headers) as client:
        # Test 1: Search Stops (No Name)
        print("\n--- Test 1: Search Stops (All) ---")
        url = f"{config.TRANSIT_BASE_URL}/stops.json"
        params = {"api-key": api_key} # No name, just generic list
        resp = await client.get(url, params=params)
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            print(f"Found {len(data.get('stops', []))} stops")
            if data.get('stops'):
                s = data['stops'][0]
                print(f"Stop 1: {s.get('name')} | Key: {s.get('key')} | Geo: {s.get('centre', {}).get('geographic', {})}")

        # Test 2: Locations benign
        print("\n--- Test 2: Locations (benign 'Main') ---")
        url = f"{config.TRANSIT_BASE_URL}/locations.json"
        params = {"api-key": api_key, "name": "Main"}
        resp = await client.get(url, params=params)
        print(f"Status: {resp.status_code}")
        if resp.status_code != 200:
             print(f"Body: {resp.text[:200]}")

        # Test 3: Stops Near (Lat/Lon)
        print("\n--- Test 3: Stops Near (Lat/Lon) ---")
        url = f"{config.TRANSIT_BASE_URL}/stops.json"
        params = {
            "api-key": api_key,
            "lat": "49.8951",
            "lon": "-97.1384",
            "distance": "500"
        }
        resp = await client.get(url, params=params)
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            print(f"Found {len(data.get('stops', []))} stops")
        else:
            print(f"Body: {resp.text[:200]}")


if __name__ == "__main__":
    asyncio.run(check_locations())
