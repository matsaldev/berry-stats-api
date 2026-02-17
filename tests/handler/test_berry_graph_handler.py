from fastapi.testclient import TestClient
from app.main import app


def test_graph_endpoint_returns_svg():
    """
    Integration test for /allBerryStats/graph endpoint.
    Ensures SVG content is returned.
    """
    with TestClient(app) as client:
        response = client.get("/allBerryStats/graph?limit=5")

        assert response.status_code == 200
        assert response.headers["content-type"] == "image/svg+xml"
        assert response.content.startswith(b"<?xml") or b"<svg" in response.content


def test_graph_endpoint_uses_cache():
    """
    Ensures graph endpoint cache works without errors.
    """
    with TestClient(app) as client:
        first = client.get("/allBerryStats/graph?limit=5")
        second = client.get("/allBerryStats/graph?limit=5")

        assert first.status_code == 200
        assert second.status_code == 200
        assert first.content == second.content
