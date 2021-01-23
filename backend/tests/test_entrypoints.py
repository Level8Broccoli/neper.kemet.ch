from fastapi.testclient import TestClient

from schemas.item import Item
from main import api

client = TestClient(api)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Version": "0.0.0"}


def test_get_all_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == []


def test_add_item():
    item = Item(name="Name", description="Description")
    response = client.post("/items/", data=item)
    assert response.status_code == 201
