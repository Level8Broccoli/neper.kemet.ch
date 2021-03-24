from pydantic import BaseModel
from uuid import UUID

class ItemRequest(BaseModel):
    name: str
    description: str


class ItemResponse(ItemRequest):
    id: UUID

    class Config:
        orm_mode = True
