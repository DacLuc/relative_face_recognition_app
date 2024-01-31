from typing import Optional
from sqlmodel import SQLModel, Field, SQLModel
import uuid
from sqlalchemy.sql.expression import func


class Ward(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs=dict(server_default=func.gen_random_uuid()),
    )
    name_ward: str = Field(index=True, nullable=False)
    id_district: uuid.UUID = Field(index=True, nullable=True, foreign_key="district.id")

    def to_dict(self):
        return {
            "id": str(self.id),
            "name_ward": self.name_ward,
            "id_district": str(self.id_district),
        }

    def json(self):
        return self.to_dict()
