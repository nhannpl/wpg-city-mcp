import os

# Transit Configuration
TRANSIT_API_KEY = os.getenv("TRANSIT_API_KEY")
TRANSIT_BASE_URL = "https://api.winnipegtransit.com/v4"
TRANSIT_STOP_SCHEDULE_URL = f"{TRANSIT_BASE_URL}/stops/{{stop_number}}/schedule.json?api-key={{api_key}}"
TRANSIT_STOPS_SEARCH_URL = f"{TRANSIT_BASE_URL}/stops.json?api-key={{api_key}}&lat={{lat}}&lon={{lon}}&distance={{distance}}"

# City Data Configuration (311)
# Using the verified 2026 dataset URL
CITY_DATA_URL = "https://data.winnipeg.ca/resource/u7f6-5326.json"

# Weather Configuration
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"
WINNIPEG_LAT = 49.8951
WINNIPEG_LON = -97.1384
