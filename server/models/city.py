from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy.sql.expression import func
import uuid


class City(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs=dict(server_default=func.gen_random_uuid()),
    )
    name_city: str = Field(index=True, nullable=False)
    id_country: uuid.UUID = Field(index=True, nullable=True, foreign_key="country.id")

    def to_dict(self):
        return {
            "id": str(self.id),
            "name_city": self.name_city,
            "id_country": str(self.id_country),
        }

    def json(self):
        return self.to_dict()
