from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

items_path = '/items/'


def test_get_all_items():
    response = client.get(items_path)
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_add_item():
    new_item = {
        'title': 'Title no 3',
        'description': 'Medium description'
    }

    response = client.post(items_path, json=new_item)
    assert response.status_code == 201
    assert response.json() == new_item
