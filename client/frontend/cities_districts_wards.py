import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import json


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
        with open("tree.json", encoding="utf-8") as f:
            self.data = json.load(f)

        provinces = [
            province["name_with_type"]
            for province in self.data.values()
            if province["type"] == "thanh-pho" or province["type"] == "tinh"
        ]
        self.city_box.addItems(provinces)

        self.update_districts()

    def update_districts(self):
        selected_province = self.city_box.currentText()
        districts = [
            district["name_with_type"]
            for province in self.data.values()
            if province["name_with_type"] == selected_province
            for district in province.get("quan-huyen", {}).values()
        ]
        self.district_box.clear()
        self.district_box.addItems(districts)
        self.update_wards()

    def update_wards(self):
        selected_district = self.district_box.currentText()
        wards = [
            ward["name_with_type"]
            for province in self.data.values()
            for district in province.get("quan-huyen", {}).values()
            if district["name_with_type"] == selected_district
            for ward in district.get("xa-phuong", {}).values()
        ]
        self.ward_box.clear()
        self.ward_box.addItems(wards)
