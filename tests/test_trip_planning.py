
import pytest
import config
from tools.trip_planning import plan_trip, plan_journey
from unittest.mock import MagicMock, patch, AsyncMock

@pytest.mark.asyncio
async def test_plan_trip_success():
    """Test planning a trip when API returns valid data."""
    mock_response_data = {
        "plans": [
            {
                "times": {"start": "2023-10-27T10:00:00", "end": "2023-10-27T10:30:00", "durations": {"total": 30}},
                "segments": [
                    {
                        "type": "walk",
                        "times": {"start": "2023-10-27T10:00:00", "end": "2023-10-27T10:05:00"},
                        "to": {"stop": {"name": "Stop A"}}
                    },
                    {
                        "type": "ride",
                        "times": {"start": "2023-10-27T10:05:00", "end": "2023-10-27T10:25:00"},
                        "route": {"key": "11", "name": "Portage"},
                        "variant": {"name": "Westwood"}
                    },
                    {
                        "type": "walk",
                        "times": {"start": "2023-10-27T10:25:00", "end": "2023-10-27T10:30:00"},
                        "to": {"intersection": {"name": "Portage at Main"}}
                    }
                ]
            }
        ]
    }

    with patch("httpx.AsyncClient") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.__aenter__.return_value = mock_instance
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_data
        
        mock_instance.get = AsyncMock(return_value=mock_response)

        result = await plan_trip("Origin", "Destination")
        
        assert "Trip: Origin -> Destination" in result
        assert "Date: 2023-10-27 10:00:00" in result
        assert "Total Duration: 30 min" in result
        assert "Walk to Stop A" in result
        assert "Ride 11 Portage (Westwood)" in result
        assert "Walk to Portage at Main" in result

@pytest.mark.asyncio
async def test_plan_trip_with_custom_mode():
    """Test that the mode parameter is correctly passed to the API."""
    mock_response_data = {
        "plans": [
            {
                "times": {"start": "2023-10-27T10:00:00", "end": "2023-10-27T10:30:00", "durations": {"total": 30}},
                "segments": []
            }
        ]
    }

    with patch("httpx.AsyncClient") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.__aenter__.return_value = mock_instance
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_data
        
        mock_instance.get = AsyncMock(return_value=mock_response)

        # Call with a specific mode
        await plan_trip("Origin", "Destination", mode="arrive-before")
        
        # Verify the 'mode' param was passed correctly
        call_args = mock_instance.get.call_args
        _, kwargs = call_args
        assert kwargs['params']['mode'] == "arrive-before"

        # Call without mode (should default to depart-after)
        await plan_trip("Origin", "Destination")
        call_args = mock_instance.get.call_args
        _, kwargs = call_args
        assert kwargs['params']['mode'] == "depart-after"

        _, kwargs = call_args
        assert kwargs['params']['mode'] == "depart-after"

@pytest.mark.asyncio
async def test_plan_trip_with_address_key():
    """Test that explicit address keys are passed through."""
    mock_response_data = {"plans": []} # No plans needed, just checking args

    with patch("httpx.AsyncClient") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.__aenter__.return_value = mock_instance
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_data
        mock_instance.get = AsyncMock(return_value=mock_response)

        await plan_trip("addresses/12345", "intersections/67890")
        
        call_args = mock_instance.get.call_args
        _, kwargs = call_args
        # Should be passed exactly as is
        assert kwargs['params']['origin'] == "addresses/12345"
        assert kwargs['params']['destination'] == "intersections/67890"

@pytest.mark.asyncio
async def test_plan_trip_landmark_resolution():
    """Test that landmarks map to correct stop keys."""
    mock_response_data = {"plans": []}

    with patch("httpx.AsyncClient") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.__aenter__.return_value = mock_instance
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_data
        mock_instance.get = AsyncMock(return_value=mock_response)

        # "Polo Park" -> "stops/10541"
        await plan_trip("Polo Park", "The Forks")
        
        call_args = mock_instance.get.call_args
        _, kwargs = call_args
        
        assert kwargs['params']['origin'] == "stops/10541"
        assert "geo/" in kwargs['params']['destination'] 

@pytest.mark.asyncio
async def test_plan_trip_no_plans():
    """Test response when no plans are found."""
    mock_response_data = {"plans": []}

    with patch("httpx.AsyncClient") as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.__aenter__.return_value = mock_instance
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_data
        mock_instance.get = AsyncMock(return_value=mock_response)

        result = await plan_trip("Home", "Work")
        
        assert "No trip plans found from Home to Work." in result

@pytest.mark.asyncio
async def test_plan_journey_success():
    """Test multi-leg journey planning."""
    # We will mock plan_trip to return a simple string for each leg to simplify this test
    # since we already tested plan_trip logic above.
    # However, plan_journey calls plan_trip, which calls the API. 
    # To test plan_journey effectively without re-testing plan_trip's internals, 
    # we can mock plan_trip itself.
    
    with patch("tools.trip_planning.plan_trip", new_callable=AsyncMock) as mock_plan_trip:
        mock_plan_trip.side_effect = [
            "Trip: A -> B\nLeg 1 details",
            "Trip: B -> C\nLeg 2 details"
        ]

        stops = ["A", "B", "C"]
        result = await plan_journey(stops)
        
        assert "--- Leg 1: A to B ---" in result
        assert "Trip: A -> B" in result
        assert "--- Leg 2: B to C ---" in result
        assert "Trip: B -> C" in result
        assert mock_plan_trip.call_count == 2

@pytest.mark.asyncio
async def test_plan_journey_insufficient_stops():
    result = await plan_journey(["A"])
    assert "Error: Need at least 2 stops" in result
