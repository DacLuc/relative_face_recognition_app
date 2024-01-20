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
    name_imagee: str = Field(index=True, nullable=False)
    image_path: str = Field(index=True, nullable=False)
    created_at: Optional[datetime] = Column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_at: Optional[datetime] = Column(
        DateTime, server_default=func.now(), nullable=False
    )
