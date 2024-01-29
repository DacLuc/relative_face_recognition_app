from typing import Optional
from sqlmodel import Field, SQLModel
import uuid
from sqlalchemy import Column, DateTime, func
from datetime import datetime


class ImageInfo(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs=dict(server_default=func.gen_random_uuid()),
    )
    id_user: uuid.UUID = Field(
        index=True, nullable=True, foreign_key="usercredentials.id"
    )
    name_image: str = Field(index=True, nullable=False)
    image_path: str = Field(index=True, nullable=False)
    created_at: Optional[datetime] = Field(default=func.now(), nullable=False)
    updated_at: Optional[datetime] = Field(default=func.now(), nullable=False)
