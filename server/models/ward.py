from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
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
    name: str = Field(index=True)
    district_id: int = Field(index=True)
