from sqlalchemy.orm import Session
from uuid import uuid4
from fastapi import Depends

from entities import item_entity
from schemas import item_schema
from storage.database import SessionLocal, engine

item_entity.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_new_item(item: item_schema.ItemRequest, db: Session = Depends(get_db)):
    random_id = str(uuid4())
    db_item = item_entity.ItemEntity(
        name=item.name,
        description=item.description,
        id=random_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return random_id


def get_all_items(db: Session = Depends(get_db)):
    all_items = db.query(item_entity.ItemEntity).all()
    return all_items
