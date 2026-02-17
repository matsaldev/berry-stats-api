import pytest
from fastapi.testclient import TestClient
from app.main import app

# Use a fixture for the test client to avoid client re-use issues
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_docs_available(client):
    response = client.get("/docs")
    assert response.status_code == 200

def test_root_stats_endpoint(client):
    response = client.get("/allBerryStats?limit=3")
    assert response.status_code == 200
