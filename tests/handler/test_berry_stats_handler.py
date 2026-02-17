from fastapi.testclient import TestClient
from app.main import app


def test_stats_endpoint_returns_json():
    """
    Integration test for /allBerryStats endpoint.
    Ensures JSON structure is returned correctly.
    """
    with TestClient(app) as client:
        response = client.get("/allBerryStats?limit=5")

        assert response.status_code == 200

        json_data = response.json()

        assert "berries_names" in json_data
        assert "min_growth_time" in json_data
        assert "max_growth_time" in json_data
        assert "mean_growth_time" in json_data
        assert "median_growth_time" in json_data
        assert "variance_growth_time" in json_data
        assert "frequency_growth_time" in json_data


def test_stats_endpoint_uses_cache():
    """
    Ensures cache is used without raising errors.
    """
    with TestClient(app) as client:
        first = client.get("/allBerryStats?limit=5")
        second = client.get("/allBerryStats?limit=5")

        assert first.status_code == 200
        assert second.status_code == 200
        assert first.json() == second.json()
