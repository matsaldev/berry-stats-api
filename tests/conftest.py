import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app instance

@pytest.fixture(scope="module")
def client():
    # Use `TestClient` within a context manager to ensure proper setup and teardown
    with TestClient(app) as c:
        yield c
