from typing import Optional
from sqlmodel import Field, SQLModel
import uuid
from sqlalchemy.sql.expression import func


class District(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs=dict(server_default=func.gen_random_uuid()),
    )
    name_district: str = Field(index=True, nullable=False)
    id_city: uuid.UUID = Field(index=True, nullable=True, foreign_key="city.id")

    def to_dict(self):
        return {
            "id": str(self.id),
            "name_district": self.name_district,
            "id_city": str(self.id_city),
        }

    def json(self):
        return self.to_dict()
