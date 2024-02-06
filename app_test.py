"""Unit test for application."""
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_read_main():
    """Returns Hello, World."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
