from app.infrastructure.http_client import ResilientHTTPClient


def test_http_client_initialization():
    client = ResilientHTTPClient()
    assert client._client is not None
