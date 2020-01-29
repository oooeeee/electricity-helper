import os
import json
import enum
import datetime
_DIR_NAME = os.path.dirname(__file__)


class AllowedDataTypes(enum.Enum):
    DAY = 'DAY'
    NIGHT = 'NIGHT'

    @classmethod
    def is_allowed(cls, string):
        for item in AllowedDataTypes:
            if item.value == string:
                return True
        return False


class Roots:
    STREETS = "STREETS"
    PRICES = "PRICES"


def get_storage_filename():
    real_data_file = os.path.join(_DIR_NAME, 'data.json')
    demo_data_file = os.path.join(_DIR_NAME, 'demo_data.json')
    return real_data_file if os.path.exists(real_data_file) else demo_data_file


class Storage:
    def __init__(self, filename=None):
        self.filename = filename or get_storage_filename()
        with open(self.filename, 'r', encoding='utf-8') as file:
            self._data = json.load(file)

    def get_street_names(self):
        return list(self._data[Roots.STREETS].keys())

    def get_street(self, street_name):
        assert street_name in self._data[Roots.STREETS], 'Unknown street name'
        return {house: house_info[-2:] for house, house_info in self._data[Roots.STREETS][street_name].items()}

    def get_house(self, street_name, house):
        street_info = self.get_street(street_name)
        assert house in street_info, 'Unknown house number'
        return street_info[house]

    def get_prices(self):
        return self._data[Roots.PRICES]

    def update_data(self, street_name, house, date, data_type, data):
        assert AllowedDataTypes.is_allowed(data_type), 'Not allowed data type'
        house_info = self.get_house(street_name, house)
        for date_info in house_info:
            if date_info['date'] == date:
                break
        else:
            raise AssertionError('Unknown date')
        date_info[data_type] = data
        self.save_storage()

    def add_today(self):
        today = datetime.datetime.now().strftime('%d.%m.%Y')
        for street_info in self._data[Roots.STREETS].values():
            for house_info in street_info.values():
                house_info.append({'date': today})
        self.save_storage()

    def save_storage(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self._data, file, indent=4, ensure_ascii=False)
