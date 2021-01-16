from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Version": "0.0.0"}


def test_get_all_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []
