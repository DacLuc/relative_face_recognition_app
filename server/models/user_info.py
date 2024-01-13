from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

class User_Info(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    image_id: Optional[int] = Field(default=None, foreign_key="image.id")
    country_id: Optional[int] = Field(default=None, foreign_key="country.id")
    city_id: Optional[int] = Field(default=None, foreign_key="city.id")
    district_id: Optional[int] = Field(default=None, foreign_key="district.id")
    ward_id: Optional[int] = Field(default=None, foreign_key="ward.id")
    name: str = Field(index=True)
    age: str = Field(index=True)
    gender: bool
    is_user: bool
    is_allowed: bool
    is_searched: bool
