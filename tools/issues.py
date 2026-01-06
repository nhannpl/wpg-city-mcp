import httpx
import config

async def search_311_issues(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$limit": 5,
        "$order": "open_date DESC" 
    }
    
    async with httpx.AsyncClient() as client:
        # Using the verified 2026 dataset URL
        response = await client.get(config.CITY_DATA_URL, params=params)
        
        if response.status_code != 200:
            return f"City API Error (Status {response.status_code}): {response.text}"

        data = response.json()

        # Type Guard: Ensure data is a list to prevent 'str' object errors
        if not isinstance(data, list):
            return "The City API returned an unexpected response format."

        if not data:
            return f"No recent issues found in the neighborhood: {neighborhood}"

        summary = []
        for item in data:
            # Extracting the most descriptive fields from your JSON sample
            issue_type = item.get('type', 'General Inquiry')
            status = item.get('case_status', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)


async def list_neighborhoods(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "$select": "neighbourhood",
        "$order": "open_date DESC",
        "$limit": 1000
    }
    
    # If a search term is provided, filter using SoQL 'like'
    if search_term:
        params["$where"] = f"upper(neighbourhood) like '%{search_term.upper()}%'"

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(config.CITY_DATA_URL, params=params)
        
        if response.status_code != 200:
            return f"Error: City API status {response.status_code}. Details: {response.text}"
            
        data = response.json()
        
        # Deduplicate and sort
        names = sorted(list(set([item.get('neighbourhood') for item in data if item.get('neighbourhood')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)
