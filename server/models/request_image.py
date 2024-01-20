from typing import Optional
from sqlmodel import Field, SQLModel
import uuid
from sqlalchemy import Column, DateTime, func
from datetime import datetime


class RequestImage(SQLModel, table=True):
    # id_request_image: day la id cua anh ma user muon yeu cau tim kiem
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs=dict(server_default=func.gen_random_uuid()),
    )
    id_user: uuid.UUID = Field(
        index=True, nullable=True, foreign_key="usercredentials.id"
    )
    file_path: str = Field(index=True, nullable=False, unique=True, max_length=255)
    created_at: Optional[datetime] = Column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Optional[datetime] = Column(
        DateTime, server_default=func.now(), nullable=False
    )
