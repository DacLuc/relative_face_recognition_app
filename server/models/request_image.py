from typing import Optional
import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Request_Image(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_info_id: Optional[int] = Field(default=None, foreign_key="user_info.id")
    updated_at: datetime.datetime = Field(
        default=datetime.datetime.now(), nullable=False)
    created_at: datetime.datetime = Field(
        default=datetime.datetime.now(), nullable=False)
