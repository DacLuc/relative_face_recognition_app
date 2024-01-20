from typing import Optional
from sqlmodel import Field, SQLModel
import uuid
from sqlalchemy.sql.expression import func


class Country(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs=dict(server_default=func.gen_random_uuid()),
    )
    name_country: str = Field(index=True, nullable=False)
