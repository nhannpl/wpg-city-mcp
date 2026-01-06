import pytest
import config
from tools.transit import get_bus_arrivals, get_commute_status
from unittest.mock import MagicMock, patch, AsyncMock

@pytest.mark.asyncio
async def test_get_bus_arrivals_success():
    """Test getting bus arrivals when API returns valid data."""
    mock_response_data = {
        "stop-schedule": {
            "route-schedules": [
                {
                    "route": {"name": "16"},
                    "scheduled-stops": [
                        {
                            "times": {
                                "arrival": {"estimated": "10:30"}
                            }
                        }
                    ]
                }
            ]
        }
    }

    # Mocking httpx.AsyncClient
    with patch("httpx.AsyncClient") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.__aenter__.return_value = mock_instance
        
        mock_response = MagicMock()
        mock_response.json.return_value = mock_response_data
        
        # When get() is called, return the mock response (make it awaitable)
        mock_instance.get = AsyncMock(return_value=mock_response)

        # Execute
        result = await get_bus_arrivals(12345)
        
        # Verify
        assert "Route 16: Arriving at 10:30" in result
        mock_instance.get.assert_called_once()
        # Verify correct URL construction
        args, _ = mock_instance.get.call_args
        assert "/stops/12345/schedule.json" in args[0]
        assert f"api-key={config.TRANSIT_API_KEY}" in args[0]

@pytest.mark.asyncio
async def test_get_bus_arrivals_no_buses():
    """Test response when no buses are scheduled."""
    mock_response_data = {
        "stop-schedule": {
            "route-schedules": []
        }
    }

    with patch("httpx.AsyncClient") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.__aenter__.return_value = mock_instance
        mock_response = MagicMock()
        mock_response.json.return_value = mock_response_data
        mock_instance.get = AsyncMock(return_value=mock_response)

        result = await get_bus_arrivals(12345)
        
        assert result == "No upcoming buses found."

@pytest.mark.asyncio
async def test_get_commute_status():
    """Test the Orchestration logic (Transit + Weather)."""
    
    # Mock Transit Data
    transit_data = {
        "stop-schedule": {
            "route-schedules": [
                {
                    "route": {"name": "16"},
                    "scheduled-stops": [{"times": {"arrival": {"estimated": "10:45"}}}]
                }
            ]
        }
    }
    
    # Mock Weather Data
    weather_data = {
        "current": {
            "temperature_2m": -20,
            "apparent_temperature": -30,
            "wind_speed_10m": 25
        }
    }

    with patch("httpx.AsyncClient") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.__aenter__.return_value = mock_instance
        
        # We need to handle two separate .get calls returning different things
        mock_transit_resp = MagicMock()
        mock_transit_resp.status_code = 200
        mock_transit_resp.json.return_value = transit_data
        
        mock_weather_resp = MagicMock()
        mock_weather_resp.status_code = 200
        mock_weather_resp.json.return_value = weather_data
        
        # Side effect creates an iterator for successive calls
        mock_instance.get = AsyncMock(side_effect=[mock_transit_resp, mock_weather_resp])

        result = await get_commute_status(12345)
        
        # Check for Weather info
        assert "-20°C" in result
        assert "Feels like -30°C" in result
        
        # Check for Bus info
        assert "Route 16: 10:45" in result
