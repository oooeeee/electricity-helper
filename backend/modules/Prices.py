from dateutil.parser import parse

demo_prices = [
    {
        "date": "01.01.2020",
        "DAY": 5.0,
        "NIGHT": 2.5
    },
    {
        "date": "01.07.2019",
        "DAY": 4.0,
        "NIGHT": 2.0
    },
    {
        "date": "01.01.2019",
        "DAY": 3.0,
        "NIGHT": 1.5
    }
]
demo_info = [
    {
        "DAY": "37040",
        "NIGHT": "17244",
        "date": "05.10.2019"
    },
    {
        "DAY": "37556",
        "NIGHT": "17382",
        "date": "03.11.2019"
    },
    {
        "DAY": "38954",
        "NIGHT": "18068",
        "date": "01.12.2019"
    },
    {
        "DAY": "41931",
        "NIGHT": "19502",
        "date": "18.01.2020"
    }
]


def parse_date(date):
    return parse(date, dayfirst=True)


class Prices:
    def __init__(self, storage):
        self.storage = storage

    def get_table_with_prices(self, street_name, house):
        house_info = self.storage.get_house(street_name, house)
        prices = self.storage.get_prices()
        result = []
        for date_info in self._order_prices_by_date(house_info):
            price_info = self._find_first_price_by_date(prices, date_info['date'])
            result.append(date_info, price_info)
            # TODO: add logic
        return house_info

    @staticmethod
    def _order_prices_by_date(prices):
        return sorted(prices, key=lambda item: parse_date(item['date']))

    @classmethod
    def _find_first_price_by_date(cls, prices, date):
        date = parse_date(date)
        for price in reversed(cls._order_prices_by_date(prices)):
            if parse_date(price['date']) < date:
                return price
