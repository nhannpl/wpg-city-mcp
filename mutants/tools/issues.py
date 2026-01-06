import httpx
import config
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result

async def x_search_311_issues__mutmut_orig(neighborhood: str) -> str:
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

async def x_search_311_issues__mutmut_1(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = None
    
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

async def x_search_311_issues__mutmut_2(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "XX$whereXX": f"upper(neighbourhood) = '{neighborhood.upper()}'",
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

async def x_search_311_issues__mutmut_3(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$WHERE": f"upper(neighbourhood) = '{neighborhood.upper()}'",
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

async def x_search_311_issues__mutmut_4(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.lower()}'",
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

async def x_search_311_issues__mutmut_5(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "XX$limitXX": 5,
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

async def x_search_311_issues__mutmut_6(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$LIMIT": 5,
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

async def x_search_311_issues__mutmut_7(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$limit": 6,
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

async def x_search_311_issues__mutmut_8(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$limit": 5,
        "XX$orderXX": "open_date DESC" 
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

async def x_search_311_issues__mutmut_9(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$limit": 5,
        "$ORDER": "open_date DESC" 
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

async def x_search_311_issues__mutmut_10(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$limit": 5,
        "$order": "XXopen_date DESCXX" 
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

async def x_search_311_issues__mutmut_11(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$limit": 5,
        "$order": "open_date desc" 
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

async def x_search_311_issues__mutmut_12(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$limit": 5,
        "$order": "OPEN_DATE DESC" 
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

async def x_search_311_issues__mutmut_13(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$limit": 5,
        "$order": "open_date DESC" 
    }
    
    async with httpx.AsyncClient() as client:
        # Using the verified 2026 dataset URL
        response = None
        
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

async def x_search_311_issues__mutmut_14(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$limit": 5,
        "$order": "open_date DESC" 
    }
    
    async with httpx.AsyncClient() as client:
        # Using the verified 2026 dataset URL
        response = await client.get(None, params=params)
        
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

async def x_search_311_issues__mutmut_15(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$limit": 5,
        "$order": "open_date DESC" 
    }
    
    async with httpx.AsyncClient() as client:
        # Using the verified 2026 dataset URL
        response = await client.get(config.CITY_DATA_URL, params=None)
        
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

async def x_search_311_issues__mutmut_16(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$limit": 5,
        "$order": "open_date DESC" 
    }
    
    async with httpx.AsyncClient() as client:
        # Using the verified 2026 dataset URL
        response = await client.get(params=params)
        
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

async def x_search_311_issues__mutmut_17(neighborhood: str) -> str:
    """Search for recent 311 service requests in a specific Winnipeg neighborhood."""
    # Using 'open_date' for ordering as confirmed by your data
    params = {
        "$where": f"upper(neighbourhood) = '{neighborhood.upper()}'",
        "$limit": 5,
        "$order": "open_date DESC" 
    }
    
    async with httpx.AsyncClient() as client:
        # Using the verified 2026 dataset URL
        response = await client.get(config.CITY_DATA_URL, )
        
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

async def x_search_311_issues__mutmut_18(neighborhood: str) -> str:
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
        
        if response.status_code == 200:
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

async def x_search_311_issues__mutmut_19(neighborhood: str) -> str:
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
        
        if response.status_code != 201:
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

async def x_search_311_issues__mutmut_20(neighborhood: str) -> str:
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

        data = None

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

async def x_search_311_issues__mutmut_21(neighborhood: str) -> str:
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
        if isinstance(data, list):
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

async def x_search_311_issues__mutmut_22(neighborhood: str) -> str:
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
            return "XXThe City API returned an unexpected response format.XX"

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

async def x_search_311_issues__mutmut_23(neighborhood: str) -> str:
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
            return "the city api returned an unexpected response format."

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

async def x_search_311_issues__mutmut_24(neighborhood: str) -> str:
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
            return "THE CITY API RETURNED AN UNEXPECTED RESPONSE FORMAT."

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

async def x_search_311_issues__mutmut_25(neighborhood: str) -> str:
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

        if data:
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

async def x_search_311_issues__mutmut_26(neighborhood: str) -> str:
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

        summary = None
        for item in data:
            # Extracting the most descriptive fields from your JSON sample
            issue_type = item.get('type', 'General Inquiry')
            status = item.get('case_status', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_27(neighborhood: str) -> str:
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
            issue_type = None
            status = item.get('case_status', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_28(neighborhood: str) -> str:
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
            issue_type = item.get(None, 'General Inquiry')
            status = item.get('case_status', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_29(neighborhood: str) -> str:
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
            issue_type = item.get('type', None)
            status = item.get('case_status', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_30(neighborhood: str) -> str:
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
            issue_type = item.get('General Inquiry')
            status = item.get('case_status', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_31(neighborhood: str) -> str:
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
            issue_type = item.get('type', )
            status = item.get('case_status', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_32(neighborhood: str) -> str:
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
            issue_type = item.get('XXtypeXX', 'General Inquiry')
            status = item.get('case_status', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_33(neighborhood: str) -> str:
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
            issue_type = item.get('TYPE', 'General Inquiry')
            status = item.get('case_status', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_34(neighborhood: str) -> str:
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
            issue_type = item.get('type', 'XXGeneral InquiryXX')
            status = item.get('case_status', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_35(neighborhood: str) -> str:
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
            issue_type = item.get('type', 'general inquiry')
            status = item.get('case_status', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_36(neighborhood: str) -> str:
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
            issue_type = item.get('type', 'GENERAL INQUIRY')
            status = item.get('case_status', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_37(neighborhood: str) -> str:
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
            status = None
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_38(neighborhood: str) -> str:
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
            status = item.get(None, 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_39(neighborhood: str) -> str:
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
            status = item.get('case_status', None)
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_40(neighborhood: str) -> str:
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
            status = item.get('N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_41(neighborhood: str) -> str:
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
            status = item.get('case_status', )
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_42(neighborhood: str) -> str:
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
            status = item.get('XXcase_statusXX', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_43(neighborhood: str) -> str:
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
            status = item.get('CASE_STATUS', 'N/A')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_44(neighborhood: str) -> str:
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
            status = item.get('case_status', 'XXN/AXX')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_45(neighborhood: str) -> str:
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
            status = item.get('case_status', 'n/a')
            # Extract just the date part (YYYY-MM-DD) from the ISO string
            raw_date = item.get('open_date', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_46(neighborhood: str) -> str:
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
            raw_date = None
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_47(neighborhood: str) -> str:
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
            raw_date = item.get(None, 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_48(neighborhood: str) -> str:
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
            raw_date = item.get('open_date', None)
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_49(neighborhood: str) -> str:
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
            raw_date = item.get('Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_50(neighborhood: str) -> str:
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
            raw_date = item.get('open_date', )
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_51(neighborhood: str) -> str:
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
            raw_date = item.get('XXopen_dateXX', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_52(neighborhood: str) -> str:
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
            raw_date = item.get('OPEN_DATE', 'Unknown Date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_53(neighborhood: str) -> str:
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
            raw_date = item.get('open_date', 'XXUnknown DateXX')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_54(neighborhood: str) -> str:
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
            raw_date = item.get('open_date', 'unknown date')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_55(neighborhood: str) -> str:
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
            raw_date = item.get('open_date', 'UNKNOWN DATE')
            date_clean = raw_date.split('T')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_56(neighborhood: str) -> str:
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
            date_clean = None
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_57(neighborhood: str) -> str:
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
            date_clean = raw_date.split(None)[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_58(neighborhood: str) -> str:
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
            date_clean = raw_date.split('XXTXX')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_59(neighborhood: str) -> str:
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
            date_clean = raw_date.split('t')[0] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_60(neighborhood: str) -> str:
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
            date_clean = raw_date.split('T')[1] if 'T' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_61(neighborhood: str) -> str:
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
            date_clean = raw_date.split('T')[0] if 'XXTXX' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_62(neighborhood: str) -> str:
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
            date_clean = raw_date.split('T')[0] if 't' in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_63(neighborhood: str) -> str:
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
            date_clean = raw_date.split('T')[0] if 'T' not in raw_date else raw_date
            
            summary.append(f"- [{date_clean}] {issue_type}: {status}")
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_64(neighborhood: str) -> str:
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
            
            summary.append(None)
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(summary)

async def x_search_311_issues__mutmut_65(neighborhood: str) -> str:
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
        
        return f"Recent 311 issues in {neighborhood}:\n" - "\n".join(summary)

async def x_search_311_issues__mutmut_66(neighborhood: str) -> str:
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
        
        return f"Recent 311 issues in {neighborhood}:\n" + "\n".join(None)

async def x_search_311_issues__mutmut_67(neighborhood: str) -> str:
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
        
        return f"Recent 311 issues in {neighborhood}:\n" + "XX\nXX".join(summary)

x_search_311_issues__mutmut_mutants : ClassVar[MutantDict] = {
'x_search_311_issues__mutmut_1': x_search_311_issues__mutmut_1, 
    'x_search_311_issues__mutmut_2': x_search_311_issues__mutmut_2, 
    'x_search_311_issues__mutmut_3': x_search_311_issues__mutmut_3, 
    'x_search_311_issues__mutmut_4': x_search_311_issues__mutmut_4, 
    'x_search_311_issues__mutmut_5': x_search_311_issues__mutmut_5, 
    'x_search_311_issues__mutmut_6': x_search_311_issues__mutmut_6, 
    'x_search_311_issues__mutmut_7': x_search_311_issues__mutmut_7, 
    'x_search_311_issues__mutmut_8': x_search_311_issues__mutmut_8, 
    'x_search_311_issues__mutmut_9': x_search_311_issues__mutmut_9, 
    'x_search_311_issues__mutmut_10': x_search_311_issues__mutmut_10, 
    'x_search_311_issues__mutmut_11': x_search_311_issues__mutmut_11, 
    'x_search_311_issues__mutmut_12': x_search_311_issues__mutmut_12, 
    'x_search_311_issues__mutmut_13': x_search_311_issues__mutmut_13, 
    'x_search_311_issues__mutmut_14': x_search_311_issues__mutmut_14, 
    'x_search_311_issues__mutmut_15': x_search_311_issues__mutmut_15, 
    'x_search_311_issues__mutmut_16': x_search_311_issues__mutmut_16, 
    'x_search_311_issues__mutmut_17': x_search_311_issues__mutmut_17, 
    'x_search_311_issues__mutmut_18': x_search_311_issues__mutmut_18, 
    'x_search_311_issues__mutmut_19': x_search_311_issues__mutmut_19, 
    'x_search_311_issues__mutmut_20': x_search_311_issues__mutmut_20, 
    'x_search_311_issues__mutmut_21': x_search_311_issues__mutmut_21, 
    'x_search_311_issues__mutmut_22': x_search_311_issues__mutmut_22, 
    'x_search_311_issues__mutmut_23': x_search_311_issues__mutmut_23, 
    'x_search_311_issues__mutmut_24': x_search_311_issues__mutmut_24, 
    'x_search_311_issues__mutmut_25': x_search_311_issues__mutmut_25, 
    'x_search_311_issues__mutmut_26': x_search_311_issues__mutmut_26, 
    'x_search_311_issues__mutmut_27': x_search_311_issues__mutmut_27, 
    'x_search_311_issues__mutmut_28': x_search_311_issues__mutmut_28, 
    'x_search_311_issues__mutmut_29': x_search_311_issues__mutmut_29, 
    'x_search_311_issues__mutmut_30': x_search_311_issues__mutmut_30, 
    'x_search_311_issues__mutmut_31': x_search_311_issues__mutmut_31, 
    'x_search_311_issues__mutmut_32': x_search_311_issues__mutmut_32, 
    'x_search_311_issues__mutmut_33': x_search_311_issues__mutmut_33, 
    'x_search_311_issues__mutmut_34': x_search_311_issues__mutmut_34, 
    'x_search_311_issues__mutmut_35': x_search_311_issues__mutmut_35, 
    'x_search_311_issues__mutmut_36': x_search_311_issues__mutmut_36, 
    'x_search_311_issues__mutmut_37': x_search_311_issues__mutmut_37, 
    'x_search_311_issues__mutmut_38': x_search_311_issues__mutmut_38, 
    'x_search_311_issues__mutmut_39': x_search_311_issues__mutmut_39, 
    'x_search_311_issues__mutmut_40': x_search_311_issues__mutmut_40, 
    'x_search_311_issues__mutmut_41': x_search_311_issues__mutmut_41, 
    'x_search_311_issues__mutmut_42': x_search_311_issues__mutmut_42, 
    'x_search_311_issues__mutmut_43': x_search_311_issues__mutmut_43, 
    'x_search_311_issues__mutmut_44': x_search_311_issues__mutmut_44, 
    'x_search_311_issues__mutmut_45': x_search_311_issues__mutmut_45, 
    'x_search_311_issues__mutmut_46': x_search_311_issues__mutmut_46, 
    'x_search_311_issues__mutmut_47': x_search_311_issues__mutmut_47, 
    'x_search_311_issues__mutmut_48': x_search_311_issues__mutmut_48, 
    'x_search_311_issues__mutmut_49': x_search_311_issues__mutmut_49, 
    'x_search_311_issues__mutmut_50': x_search_311_issues__mutmut_50, 
    'x_search_311_issues__mutmut_51': x_search_311_issues__mutmut_51, 
    'x_search_311_issues__mutmut_52': x_search_311_issues__mutmut_52, 
    'x_search_311_issues__mutmut_53': x_search_311_issues__mutmut_53, 
    'x_search_311_issues__mutmut_54': x_search_311_issues__mutmut_54, 
    'x_search_311_issues__mutmut_55': x_search_311_issues__mutmut_55, 
    'x_search_311_issues__mutmut_56': x_search_311_issues__mutmut_56, 
    'x_search_311_issues__mutmut_57': x_search_311_issues__mutmut_57, 
    'x_search_311_issues__mutmut_58': x_search_311_issues__mutmut_58, 
    'x_search_311_issues__mutmut_59': x_search_311_issues__mutmut_59, 
    'x_search_311_issues__mutmut_60': x_search_311_issues__mutmut_60, 
    'x_search_311_issues__mutmut_61': x_search_311_issues__mutmut_61, 
    'x_search_311_issues__mutmut_62': x_search_311_issues__mutmut_62, 
    'x_search_311_issues__mutmut_63': x_search_311_issues__mutmut_63, 
    'x_search_311_issues__mutmut_64': x_search_311_issues__mutmut_64, 
    'x_search_311_issues__mutmut_65': x_search_311_issues__mutmut_65, 
    'x_search_311_issues__mutmut_66': x_search_311_issues__mutmut_66, 
    'x_search_311_issues__mutmut_67': x_search_311_issues__mutmut_67
}

def search_311_issues(*args, **kwargs):
    result = _mutmut_trampoline(x_search_311_issues__mutmut_orig, x_search_311_issues__mutmut_mutants, args, kwargs)
    return result 

search_311_issues.__signature__ = _mutmut_signature(x_search_311_issues__mutmut_orig)
x_search_311_issues__mutmut_orig.__name__ = 'x_search_311_issues'


async def x_list_neighborhoods__mutmut_orig(search_term: str = None) -> str:
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


async def x_list_neighborhoods__mutmut_1(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = None
    
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


async def x_list_neighborhoods__mutmut_2(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "XX$selectXX": "neighbourhood",
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


async def x_list_neighborhoods__mutmut_3(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "$SELECT": "neighbourhood",
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


async def x_list_neighborhoods__mutmut_4(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "$select": "XXneighbourhoodXX",
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


async def x_list_neighborhoods__mutmut_5(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "$select": "NEIGHBOURHOOD",
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


async def x_list_neighborhoods__mutmut_6(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "$select": "neighbourhood",
        "XX$orderXX": "open_date DESC",
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


async def x_list_neighborhoods__mutmut_7(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "$select": "neighbourhood",
        "$ORDER": "open_date DESC",
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


async def x_list_neighborhoods__mutmut_8(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "$select": "neighbourhood",
        "$order": "XXopen_date DESCXX",
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


async def x_list_neighborhoods__mutmut_9(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "$select": "neighbourhood",
        "$order": "open_date desc",
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


async def x_list_neighborhoods__mutmut_10(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "$select": "neighbourhood",
        "$order": "OPEN_DATE DESC",
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


async def x_list_neighborhoods__mutmut_11(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "$select": "neighbourhood",
        "$order": "open_date DESC",
        "XX$limitXX": 1000
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


async def x_list_neighborhoods__mutmut_12(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "$select": "neighbourhood",
        "$order": "open_date DESC",
        "$LIMIT": 1000
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


async def x_list_neighborhoods__mutmut_13(search_term: str = None) -> str:
    """
    Get a list of Winnipeg neighborhoods that have had recent 311 activity.
    Optionally filter by a search_term (e.g., 'Fort').
    """
    # Performance Note: 'distinct' queries on the large 311 dataset are too slow.
    # Instead, we fetch the 1000 most recent requests and deduplicate the neighborhoods in Python.
    params = {
        "$select": "neighbourhood",
        "$order": "open_date DESC",
        "$limit": 1001
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


async def x_list_neighborhoods__mutmut_14(search_term: str = None) -> str:
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
        params["$where"] = None

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


async def x_list_neighborhoods__mutmut_15(search_term: str = None) -> str:
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
        params["XX$whereXX"] = f"upper(neighbourhood) like '%{search_term.upper()}%'"

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


async def x_list_neighborhoods__mutmut_16(search_term: str = None) -> str:
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
        params["$WHERE"] = f"upper(neighbourhood) like '%{search_term.upper()}%'"

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


async def x_list_neighborhoods__mutmut_17(search_term: str = None) -> str:
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
        params["$where"] = f"upper(neighbourhood) like '%{search_term.lower()}%'"

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


async def x_list_neighborhoods__mutmut_18(search_term: str = None) -> str:
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

    async with httpx.AsyncClient(timeout=None) as client:
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


async def x_list_neighborhoods__mutmut_19(search_term: str = None) -> str:
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

    async with httpx.AsyncClient(timeout=31.0) as client:
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


async def x_list_neighborhoods__mutmut_20(search_term: str = None) -> str:
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
        response = None
        
        if response.status_code != 200:
            return f"Error: City API status {response.status_code}. Details: {response.text}"
            
        data = response.json()
        
        # Deduplicate and sort
        names = sorted(list(set([item.get('neighbourhood') for item in data if item.get('neighbourhood')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_21(search_term: str = None) -> str:
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
        response = await client.get(None, params=params)
        
        if response.status_code != 200:
            return f"Error: City API status {response.status_code}. Details: {response.text}"
            
        data = response.json()
        
        # Deduplicate and sort
        names = sorted(list(set([item.get('neighbourhood') for item in data if item.get('neighbourhood')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_22(search_term: str = None) -> str:
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
        response = await client.get(config.CITY_DATA_URL, params=None)
        
        if response.status_code != 200:
            return f"Error: City API status {response.status_code}. Details: {response.text}"
            
        data = response.json()
        
        # Deduplicate and sort
        names = sorted(list(set([item.get('neighbourhood') for item in data if item.get('neighbourhood')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_23(search_term: str = None) -> str:
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
        response = await client.get(params=params)
        
        if response.status_code != 200:
            return f"Error: City API status {response.status_code}. Details: {response.text}"
            
        data = response.json()
        
        # Deduplicate and sort
        names = sorted(list(set([item.get('neighbourhood') for item in data if item.get('neighbourhood')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_24(search_term: str = None) -> str:
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
        response = await client.get(config.CITY_DATA_URL, )
        
        if response.status_code != 200:
            return f"Error: City API status {response.status_code}. Details: {response.text}"
            
        data = response.json()
        
        # Deduplicate and sort
        names = sorted(list(set([item.get('neighbourhood') for item in data if item.get('neighbourhood')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_25(search_term: str = None) -> str:
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
        
        if response.status_code == 200:
            return f"Error: City API status {response.status_code}. Details: {response.text}"
            
        data = response.json()
        
        # Deduplicate and sort
        names = sorted(list(set([item.get('neighbourhood') for item in data if item.get('neighbourhood')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_26(search_term: str = None) -> str:
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
        
        if response.status_code != 201:
            return f"Error: City API status {response.status_code}. Details: {response.text}"
            
        data = response.json()
        
        # Deduplicate and sort
        names = sorted(list(set([item.get('neighbourhood') for item in data if item.get('neighbourhood')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_27(search_term: str = None) -> str:
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
            
        data = None
        
        # Deduplicate and sort
        names = sorted(list(set([item.get('neighbourhood') for item in data if item.get('neighbourhood')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_28(search_term: str = None) -> str:
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
        names = None
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_29(search_term: str = None) -> str:
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
        names = sorted(None)
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_30(search_term: str = None) -> str:
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
        names = sorted(list(None))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_31(search_term: str = None) -> str:
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
        names = sorted(list(set(None)))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_32(search_term: str = None) -> str:
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
        names = sorted(list(set([item.get(None) for item in data if item.get('neighbourhood')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_33(search_term: str = None) -> str:
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
        names = sorted(list(set([item.get('XXneighbourhoodXX') for item in data if item.get('neighbourhood')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_34(search_term: str = None) -> str:
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
        names = sorted(list(set([item.get('NEIGHBOURHOOD') for item in data if item.get('neighbourhood')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_35(search_term: str = None) -> str:
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
        names = sorted(list(set([item.get('neighbourhood') for item in data if item.get(None)])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_36(search_term: str = None) -> str:
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
        names = sorted(list(set([item.get('neighbourhood') for item in data if item.get('XXneighbourhoodXX')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_37(search_term: str = None) -> str:
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
        names = sorted(list(set([item.get('neighbourhood') for item in data if item.get('NEIGHBOURHOOD')])))
        
        if not names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_38(search_term: str = None) -> str:
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
        
        if names:
            return f"No neighborhoods found matching '{search_term}'."
            
        # Clean up the output for the AI
        return "Neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_39(search_term: str = None) -> str:
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
        return "Neighborhoods (from recent activity):\n" - "\n".join(names)


async def x_list_neighborhoods__mutmut_40(search_term: str = None) -> str:
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
        return "XXNeighborhoods (from recent activity):\nXX" + "\n".join(names)


async def x_list_neighborhoods__mutmut_41(search_term: str = None) -> str:
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
        return "neighborhoods (from recent activity):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_42(search_term: str = None) -> str:
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
        return "NEIGHBORHOODS (FROM RECENT ACTIVITY):\n" + "\n".join(names)


async def x_list_neighborhoods__mutmut_43(search_term: str = None) -> str:
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
        return "Neighborhoods (from recent activity):\n" + "\n".join(None)


async def x_list_neighborhoods__mutmut_44(search_term: str = None) -> str:
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
        return "Neighborhoods (from recent activity):\n" + "XX\nXX".join(names)

x_list_neighborhoods__mutmut_mutants : ClassVar[MutantDict] = {
'x_list_neighborhoods__mutmut_1': x_list_neighborhoods__mutmut_1, 
    'x_list_neighborhoods__mutmut_2': x_list_neighborhoods__mutmut_2, 
    'x_list_neighborhoods__mutmut_3': x_list_neighborhoods__mutmut_3, 
    'x_list_neighborhoods__mutmut_4': x_list_neighborhoods__mutmut_4, 
    'x_list_neighborhoods__mutmut_5': x_list_neighborhoods__mutmut_5, 
    'x_list_neighborhoods__mutmut_6': x_list_neighborhoods__mutmut_6, 
    'x_list_neighborhoods__mutmut_7': x_list_neighborhoods__mutmut_7, 
    'x_list_neighborhoods__mutmut_8': x_list_neighborhoods__mutmut_8, 
    'x_list_neighborhoods__mutmut_9': x_list_neighborhoods__mutmut_9, 
    'x_list_neighborhoods__mutmut_10': x_list_neighborhoods__mutmut_10, 
    'x_list_neighborhoods__mutmut_11': x_list_neighborhoods__mutmut_11, 
    'x_list_neighborhoods__mutmut_12': x_list_neighborhoods__mutmut_12, 
    'x_list_neighborhoods__mutmut_13': x_list_neighborhoods__mutmut_13, 
    'x_list_neighborhoods__mutmut_14': x_list_neighborhoods__mutmut_14, 
    'x_list_neighborhoods__mutmut_15': x_list_neighborhoods__mutmut_15, 
    'x_list_neighborhoods__mutmut_16': x_list_neighborhoods__mutmut_16, 
    'x_list_neighborhoods__mutmut_17': x_list_neighborhoods__mutmut_17, 
    'x_list_neighborhoods__mutmut_18': x_list_neighborhoods__mutmut_18, 
    'x_list_neighborhoods__mutmut_19': x_list_neighborhoods__mutmut_19, 
    'x_list_neighborhoods__mutmut_20': x_list_neighborhoods__mutmut_20, 
    'x_list_neighborhoods__mutmut_21': x_list_neighborhoods__mutmut_21, 
    'x_list_neighborhoods__mutmut_22': x_list_neighborhoods__mutmut_22, 
    'x_list_neighborhoods__mutmut_23': x_list_neighborhoods__mutmut_23, 
    'x_list_neighborhoods__mutmut_24': x_list_neighborhoods__mutmut_24, 
    'x_list_neighborhoods__mutmut_25': x_list_neighborhoods__mutmut_25, 
    'x_list_neighborhoods__mutmut_26': x_list_neighborhoods__mutmut_26, 
    'x_list_neighborhoods__mutmut_27': x_list_neighborhoods__mutmut_27, 
    'x_list_neighborhoods__mutmut_28': x_list_neighborhoods__mutmut_28, 
    'x_list_neighborhoods__mutmut_29': x_list_neighborhoods__mutmut_29, 
    'x_list_neighborhoods__mutmut_30': x_list_neighborhoods__mutmut_30, 
    'x_list_neighborhoods__mutmut_31': x_list_neighborhoods__mutmut_31, 
    'x_list_neighborhoods__mutmut_32': x_list_neighborhoods__mutmut_32, 
    'x_list_neighborhoods__mutmut_33': x_list_neighborhoods__mutmut_33, 
    'x_list_neighborhoods__mutmut_34': x_list_neighborhoods__mutmut_34, 
    'x_list_neighborhoods__mutmut_35': x_list_neighborhoods__mutmut_35, 
    'x_list_neighborhoods__mutmut_36': x_list_neighborhoods__mutmut_36, 
    'x_list_neighborhoods__mutmut_37': x_list_neighborhoods__mutmut_37, 
    'x_list_neighborhoods__mutmut_38': x_list_neighborhoods__mutmut_38, 
    'x_list_neighborhoods__mutmut_39': x_list_neighborhoods__mutmut_39, 
    'x_list_neighborhoods__mutmut_40': x_list_neighborhoods__mutmut_40, 
    'x_list_neighborhoods__mutmut_41': x_list_neighborhoods__mutmut_41, 
    'x_list_neighborhoods__mutmut_42': x_list_neighborhoods__mutmut_42, 
    'x_list_neighborhoods__mutmut_43': x_list_neighborhoods__mutmut_43, 
    'x_list_neighborhoods__mutmut_44': x_list_neighborhoods__mutmut_44
}

def list_neighborhoods(*args, **kwargs):
    result = _mutmut_trampoline(x_list_neighborhoods__mutmut_orig, x_list_neighborhoods__mutmut_mutants, args, kwargs)
    return result 

list_neighborhoods.__signature__ = _mutmut_signature(x_list_neighborhoods__mutmut_orig)
x_list_neighborhoods__mutmut_orig.__name__ = 'x_list_neighborhoods'
