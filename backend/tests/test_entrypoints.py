from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Status": "online"}


def test_get_all_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_one_item():
    response = client.get("/items/00000000-0000-0000-0000-000000000000/")
    assert response.status_code == 200
    assert "name" in response.json()
    assert "description" in response.json()
    assert "id" in response.json()


def test_post_one_item():
    item = {"name": "Itemname", "description": "Short Description"}
    response = client.post(
        "/items/",
        json=item)
    assert response.status_code == 201
    assert response.json() == {
        **item, "id": "00000000-0000-0000-0000-000000000000"}


def test_post_one_illegal_item():
    response = client.post(
        "/items/",
        json={"names": "Itemname", "description": "Short Description"})
    assert response.status_code == 422


def test_post_one_item_missing_attribute():
    response = client.post(
        "/items/",
        json={"name": "Itemname"})
    assert response.status_code == 422


def test_delete_one_item():
    response = client.delete(
        "/items/00000000-0000-0000-0000-000000000000/"
    )
    assert response.status_code == 200
