from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/items',
    tags=['items']
)

db = [
    {
        'id': 0,
        'title': 'Item 0',
        'description': 'Kurze Beschreibung zum Item Nr. 0',
    }, {
        'id': 1,
        'title': 'Item 1',
        'description': 'Kurze Beschreibung zum Item Nr. 1',
    }
]


@router.get('')
def get_all_items():
    return db


@router.get('/{id}')
def get_item(id: int):
    return db[id]


class NewItem(BaseModel):
    title: str
    description: str


@router.post('', status_code=201)
def add_item(item: NewItem):
    new_id = len(db)
    db.append({'id': new_id, 'title': item.title,
              'description': item.description})
    return db[new_id]
