from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Image(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    image_id: str = Field(index=True)
