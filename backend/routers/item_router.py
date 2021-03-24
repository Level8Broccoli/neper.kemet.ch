from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from uuid import UUID

from schemas.item_schema import ItemRequest, ItemResponse
from services import items_service
from storage.database import SessionLocal

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ItemResponse])
def get_all_items(db: Session = Depends(get_db)):
    return items_service.get_all_items(db=db)

@router.get("/{id}/", response_model=ItemResponse)
def get_item(id: UUID):
    return ItemResponse(name="Name", description="Short Description", id="00000000-0000-0000-0000-000000000000")


@router.post("/", status_code=201, response_model=ItemResponse)
def create_new_item(item: ItemRequest, db: Session = Depends(get_db)):
    id = items_service.create_new_item(item, db=db)
    return ItemResponse(name=item.name, description=item.description, id=id)


@router.delete("/{id}/")
def delete_item(id: UUID):
    pass
