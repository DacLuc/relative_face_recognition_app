from PyQt6 import QtWidgets, QtCore
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

        self.selected_country_id = None
        self.selected_city_id = None
        self.selected_district_id = None
        self.selected_ward_id = None

        self.load_data()

        self.city_box.currentIndexChanged.connect(self.update_districts)
        self.district_box.currentIndexChanged.connect(self.update_wards)
        self.ward_box.currentIndexChanged.connect(self.update_selected_ward_id)

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
            if country:
                self.selected_country_id = country.id  # Store the selected country id
                cities = session.exec(
                    select(City).where(City.id_country == country.id)
                ).all()

                self.city_box.clear()
                self.city_box.addItems([city.name_city for city in cities])
            else:
                # Handle the case where no matching country is found
                print("No matching country found for:", selected_country)
        self.update_districts()

    def update_districts(self):
        selected_city = self.city_box.currentText()

        with Session(engine) as session:
            city = session.exec(
                select(City).where(City.name_city == selected_city)
            ).first()

            if city:
                self.selected_city_id = city.id  # Store the selected city id
                districts = session.exec(
                    select(District).where(District.id_city == city.id)
                ).all()
                self.district_box.clear()
                self.district_box.addItems(
                    [district.name_district for district in districts]
                )
            else:
                # Handle the case where no matching city is found
                print("No matching city found for:", selected_city)
        self.update_wards()

    def update_wards(self):
        selected_district = self.district_box.currentText()

        with Session(engine) as session:
            district = session.exec(
                select(District).where(District.name_district == selected_district)
            ).first()
            if district:
                self.selected_district_id = (
                    district.id
                )  # Store the selected district id
                wards = session.exec(
                    select(Ward).where(Ward.id_district == district.id)
                ).all()

                self.ward_box.clear()
                ward_names = [ward.name_ward for ward in wards]
                self.ward_box.addItems(ward_names)

                # Check if there are wards and set selected_ward_id
                if wards:
                    self.selected_ward_id = wards[
                        0
                    ].id  # Set the default to the first ward
                else:
                    self.selected_ward_id = None
                    print("No wards found for district:", selected_district)
            else:
                # Handle the case where no matching district is found
                print("No matching district found for:", selected_district)

    def update_selected_ward_id(self):
        selected_ward = self.ward_box.currentText()

        with Session(engine) as session:
            ward = session.exec(
                select(Ward).where(Ward.name_ward == selected_ward)
            ).first()
            if ward:
                self.selected_ward_id = ward.id
            else:
                print("No matching ward found for:", selected_ward)
