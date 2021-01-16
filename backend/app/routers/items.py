from fastapi import APIRouter
from typing import List

from schemas.item import Item

router = APIRouter(
    prefix="/items",
    tags=["items"]
)


@router.get("/", response_model=List[Item])
def get_all_items():
    return []
