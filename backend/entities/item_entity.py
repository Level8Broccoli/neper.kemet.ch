from sqlalchemy import Column, String

from storage.database import Base


class ItemEntity(Base):
    __tablename__ = "items"

    id = Column(
        String,
        primary_key=True,
        index=True,
        unique=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
