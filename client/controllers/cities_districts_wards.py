from PyQt6 import QtWidgets
import sys
import os

from sqlmodel import Session, select

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")
from server.database.engine import *
from server.models.user_info import *
from server.models.user_credentials import *
from server.models.image_info import *
from server.models.country import *
from server.models.city import *
from server.models.district import *
from server.models.ward import *


class LocationApp(QtWidgets.QWidget):
    def __init__(self, nation_box, city_box, district_box, ward_box):
        super().__init__()

        self.nation_box = nation_box
        self.city_box = city_box
        self.district_box = district_box
        self.ward_box = ward_box

        self.load_data()

        self.city_box.currentIndexChanged.connect(self.update_districts)
        self.district_box.currentIndexChanged.connect(self.update_wards)

    def load_data(self):
        with Session(engine) as session:
            countries = session.exec(select(Country)).all()
            self.nation_box.addItems([country.name_country for country in countries])

        self.update_cities()

    def update_cities(self):
        selected_country = self.nation_box.currentText()

        with Session(engine) as session:
            country = session.exec(
                select(Country).where(Country.name_country == selected_country)
            ).first()
            cities = session.exec(
                select(City).where(City.id_country == country.id)
            ).all()

            self.city_box.clear()
            self.city_box.addItems([city.name_city for city in cities])

        self.update_districts()

    def update_districts(self):
        selected_city = self.city_box.currentText()

        with Session(engine) as session:
            city = session.exec(
                select(City).where(City.name_city == selected_city)
            ).first()

            if city:
                districts = session.exec(
                    select(District).where(District.id_city == city.id)
                ).all()
                self.district_box.clear()
                self.district_box.addItems(
                    [district.name_district for district in districts]
                )
                self.update_wards()
            else:
                # Handle the case where no matching city is found
                print("No matching city found for:", selected_city)

    def update_wards(self):
        selected_district = self.district_box.currentText()

        with Session(engine) as session:
            district = session.exec(
                select(District).where(District.name_district == selected_district)
            ).first()
            if district:
                wards = session.exec(
                    select(Ward).where(Ward.id_district == district.id)
                ).all()

                self.ward_box.clear()
                self.ward_box.addItems([ward.name_ward for ward in wards])
            else:
                # Handle the case where no matching district is found
                print("No matching district found for:", selected_district)
