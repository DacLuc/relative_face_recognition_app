from typing import Optional, List
from sqlmodel import Field, SQLModel
import uuid
from sqlalchemy import Column, func
from datetime import datetime
from pgvector.sqlalchemy import Vector


class ImageInfo(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs=dict(server_default=func.gen_random_uuid()),
    )
    id_user: uuid.UUID = Field(
        index=True, nullable=True, unique=True, foreign_key="usercredentials.id"
    )
    image_name: Optional[str] = Field(nullable=True, max_length=255)
    image_path: Optional[str] = Field(nullable=True, unique=True, max_length=255)
    embeddings: List[float] = Field(sa_column=Column(Vector(512)))
    created_at: Optional[datetime] = Field(default=func.now(), nullable=False)
    updated_at: Optional[datetime] = Field(default=func.now(), nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "id_user": str(self.id_user),
            "image_name": self.image_name,
            "image_path": self.image_path,
            "embeddings": self.embeddings,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def json(self):
        return self.to_dict()
