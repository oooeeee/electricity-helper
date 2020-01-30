from .common import parse_date


class Prices:
    def __init__(self, storage, price_types):
        self.storage = storage
        self.price_types = price_types

    def get_table_with_prices(self, street_name, house):
        house_info = self.storage.get_house(street_name, house)
        rates = self.storage.get_prices()
        return self._get_table_info(house_info, rates)

    def _get_table_info(self, house_info, rates):
        dicts = []
        header = []
        prev_date_info = {}
        for date_info in self._order_prices_by_date(house_info):
            price_info = self._find_first_price_by_date(rates, date_info['date'])
            result_row = {'Date': date_info['date']}
            total = 0.0
            prev_date_info = prev_date_info or date_info
            for price_type in self.price_types:
                kwt = int(date_info.get(price_type) or 0)
                delta_kwt = kwt - int(prev_date_info.get(price_type) or 0)
                result_row[f"{price_type} KWH"] = kwt
                result_row[f"{price_type} KWH delta"] = delta_kwt
                result_row[f"{price_type} rate"] = rate = price_info[price_type]
                result_row[f"{price_type} price"] = price = round(delta_kwt * rate, 2)
                total += price
            result_row["Total"] = round(total, 2)
            prev_date_info = date_info
            header = header or list(result_row.keys())
            dicts.append(result_row)
        return [header] + [[row[head] for head in header] for row in dicts]

    @staticmethod
    def _order_prices_by_date(prices):
        return sorted(prices, key=lambda item: parse_date(item['date']))

    @classmethod
    def _find_first_price_by_date(cls, prices, date):
        date = parse_date(date)
        for price in reversed(cls._order_prices_by_date(prices)):
            if parse_date(price['date']) < date:
                return price
