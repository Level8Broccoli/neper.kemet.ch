from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str


class Item(ItemBase):
    pass
