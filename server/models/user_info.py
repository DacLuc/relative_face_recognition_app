from typing import Optional
from sqlmodel import Field, SQLModel
import uuid
from sqlalchemy import func
from datetime import datetime


# Anh Huy dan la chi khi nao cac field co truong du lieu dung de sort, insert, update, delete thi ta moi dung index=True
# UserInfo(id, id_user, name, age, gender, id_request_image, id_country, id_city, id_district, id_ward, is_finding_user, is_allowed, is_searched)
# --> day la table de luu thong tin cua user sau khi dang nhap (bang nay co 2 chuc nang chinh la: luu du lieu cua user duoc tim va user dang tim kiem nguoi khac --> ta xem user dang tim va user duoc tim thuoc cung mot truong du lieu la user_info)
# --> Muon biet duoc users nao la nguoi dang tim va user nao dang duoc tim thi ta se dung 2 cot la is_finding_user va is_searched_user (neu is_finding_user = True thi user do dang tim kiem nguoi khac, nguoc lai neu is_searched_user = True thi user do dang duoc tim kiem)
class UserInfo(SQLModel, table=True):
    # id_user_info: la id cua user khi nhap thong tin ca nhan vao app
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs=dict(server_default=func.gen_random_uuid()),
    )
    # id_user: la id cua tai khoan user trong bang user_credentials()
    id_user: uuid.UUID = Field(
        nullable=True, index=True, unique=True, foreign_key="usercredentials.id"
    )
    # name: day la ho va ten cua user khi nhap thong tin ca nhan chu khong phai username khi user dang nhap / dang ky
    full_name: str = Field(nullable=False)
    # age: em khong chac nen de kieu du lieu gi -> nhung ma theo ui thi em su dung radiobutton de lua chon age-range nen anh check xem du lieu nao hop ly nhat
    age: int = Field(index=True, nullable=False)
    # gender: anh chi co the lua chon mot trong hai kieu du lieu la "Nam" hay "Nu" --> thong thuong theo hoc tren truong em se de la kieu nvarchar(3) de luu du lieu nay nhung trong sqlmodel thi em khong chac nen de kieu du lieu string hay khong ?
    gender: bool = Field(nullable=False)
    # id_image: day la id cua anh ma user nhap khi vao trang thong tin ca nhan vao app
    id_image: uuid.UUID = Field(
        nullable=True, index=True, unique=True, foreign_key="imageinfo.id"
    )
    # id_country: day la id cua quoc gia ma users nhap khi vao trang thong tin ca nhan vao app
    # FK (Foreign_Key): User_info(id_country) --> Country(id)
    id_country: uuid.UUID = Field(index=True, nullable=True, foreign_key="country.id")
    # id_city: day la id cua thanh pho / tinh thanh ma users nhap khi vao trang thong tin ca nhan vao app
    # FK (Foreign_Key): User_info(id_city) --> City(id)
    id_city: uuid.UUID = Field(index=True, nullable=True, foreign_key="city.id")
    # id_district: day la id cua quan / huyen ma users nhap khi vao trang thong tin ca nhan vao app
    # FK (Foreign_Key): User_info(id_district) --> District(id)
    id_district: uuid.UUID = Field(index=True, nullable=True, foreign_key="district.id")
    # id_ward: day la id cua phuong / xa ma users nhap khi vao trang thong tin ca nhan vao app
    # FK (Foreign_Key): User_info(id_ward) --> Ward(id)
    id_ward: uuid.UUID = Field(index=True, nullable=True, foreign_key="ward.id")
    # face_feature: day la dac trung khuon mat cua user khi nhap thong tin ca nhan vao app
    face_feature: str = Field(nullable=True)
    # is_finding_user: check xem user nay dang tim kiem nguoi khac hay khong
    is_finding_user: bool = Field(nullable=True)
    # is_allowed: check xem user nay co cho phep nguoi khac tim kiem minh hay khong
    is_allowed: bool = Field(index=True, nullable=True)
    # is_searched: check xem user nay dang duoc tim kiem hay khong
    is_searched_user: bool = Field(nullable=True)
    # created_at: thoi diem tao tai khoan user_info
    created_at: Optional[datetime] = Field(default=func.now(), nullable=False)
    # updated_at: thoi diem cap nhat tai khoan user_info
    updated_at: Optional[datetime] = Field(default=func.now(), nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "id_user": str(self.id_user),
            "full_name": self.full_name,
            "age": self.age,
            "gender": "Nam" if self.gender else "Nữ",
            "id_image": str(self.id_image),
            "id_country": str(self.id_country),
            "id_city": str(self.id_city),
            "id_district": str(self.id_district),
            "id_ward": str(self.id_ward),
            "face_feature": self.face_feature,
            "is_finding_user": self.is_finding_user,
            "is_allowed": self.is_allowed,
            "is_searched_user": self.is_searched_user,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def json(self):
        return self.to_dict()
