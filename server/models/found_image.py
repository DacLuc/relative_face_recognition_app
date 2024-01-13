from typing import Optional
import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Found_Image(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    finder_id: Optional[int] = Field(default=None, foreign_key="user.id")
    updated_at: datetime.datetime = Field(
        default=datetime.datetime.now(), nullable=False)
    created_at: datetime.datetime = Field(
        default=datetime.datetime.now(), nullable=False)
