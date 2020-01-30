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


def _house_order(house):
    house = f"{house}0" if isinstance(house, int) or (isinstance(house, str) and house.isdigit()) else house
    return f"{house:0>30}"


def sort_houses(houses):
    return sorted(houses, key=_house_order)


def test_sort_houses():
    assert sort_houses([1, 10, 2, '20', 11, 12, '11a', '30a', 30]) == [1, 2, 10, 11, '11a', 12, '20', 30, '30a']


if __name__ == '__main__':
    test_sort_houses()
