from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/items',
    tags=['items']
)


@router.get('/')
def get_all_items():
    return [
        {
            'title': 'Item 1',
            'description': 'Short description'
        }, {
            'title': 'Item 2',
            'description': 'Longer description'
        },
    ]


class NewItem(BaseModel):
    title: str
    description: str


@router.post('/', status_code=201)
def add_item(item: NewItem):
    return item
