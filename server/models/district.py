from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select


class District(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
