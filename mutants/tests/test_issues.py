import pytest
import config
from tools.issues import search_311_issues, list_neighborhoods
from unittest.mock import MagicMock, patch, AsyncMock

@pytest.mark.asyncio
async def test_search_311_issues_found():
    """Test searching 311 issues when data is found."""
    mock_data = [
        {
            "type": "Pothole",
            "case_status": "Open",
            "open_date": "2025-05-20T10:00:00"
        }
    ]

    with patch("httpx.AsyncClient") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.__aenter__.return_value = mock_instance
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_instance.get = AsyncMock(return_value=mock_response)

        result = await search_311_issues("Downtown")
        
        assert "Recent 311 issues in Downtown" in result
        assert "Pothole" in result
        assert "2025-05-20" in result
        
        # Verify parameters passed to API
        args, kwargs = mock_instance.get.call_args
        assert kwargs['params']['$where'] == "upper(neighbourhood) = 'DOWNTOWN'"

@pytest.mark.asyncio
async def test_search_311_issues_empty():
    """Test searching 311 issues when none are found."""
    with patch("httpx.AsyncClient") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.__aenter__.return_value = mock_instance
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_instance.get = AsyncMock(return_value=mock_response)

        result = await search_311_issues("Ghost Town")
        assert "No recent issues found in the neighborhood: Ghost Town" in result

@pytest.mark.asyncio
async def test_list_neighborhoods_logic():
    """Test neighborhood deduplication and searching logic."""
    # Data has duplicates and mixed casing, unsorted
    mock_data = [
        {"neighbourhood": "West End"},
        {"neighbourhood": "west end"}, # Duplicate (if we were strictly normalizing, but set() handles exact strings)
        {"neighbourhood": "Downtown"},
        {"neighbourhood": "West End"}
    ]
    # Note: The tool implementation currently does minimal string normalization before set(),
    # it relies on the API return. In the test data above, "west end" and "West End" are different strings.
    # The tool code: set([item.get('neighbourhood')...])
    
    with patch("httpx.AsyncClient") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.__aenter__.return_value = mock_instance
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_instance.get = AsyncMock(return_value=mock_response)

        result = await list_neighborhoods()
        
        assert "Neighborhoods (from recent activity):" in result
        assert "Downtown" in result
        assert "West End" in result
