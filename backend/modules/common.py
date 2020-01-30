import enum
from dateutil.parser import parse


class AllowedDataTypes(enum.Enum):
    DAY = 'DAY'
    NIGHT = 'NIGHT'

    @classmethod
    def is_allowed(cls, string):
        for item in AllowedDataTypes:
            if item.value == string:
                return True
        return False


def parse_date(date):
    return parse(date, dayfirst=True)


def sort_house_info(house_info):
    return sorted(house_info, key=lambda item: parse_date(item['date']))
