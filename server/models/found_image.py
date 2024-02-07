from typing import Optional, List
from sqlmodel import Field, SQLModel
import uuid
from sqlalchemy import Column, DateTime, func
from datetime import datetime
from pgvector.sqlalchemy import Vector


class FoundImage(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs=dict(server_default=func.gen_random_uuid()),
    )
    id_request_image: uuid.UUID = Field(
        default=None, nullable=True, index=True, foreign_key="requestimage.id"
    )
    id_found_image: uuid.UUID = Field(
        default=None, nullable=True, index=True, foreign_key="imageinfo.id"
    )
    found_time: float = Field(default=None, nullable=True)
    similarity_faces: List[float] = Field(sa_column=Column(Vector(5)))
    created_at: Optional[datetime] = Column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Optional[datetime] = Column(
        DateTime, server_default=func.now(), nullable=False
    )
    id_user_info: uuid.UUID = Field(
        default=None, nullable=True, index=True, foreign_key="userinfo.id"
    )
