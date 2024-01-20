import requests


def call_api(url: str, data):
    return requests.post(url, headers={"Content-Type": "application/json"}, json=data)


STOCK_URL = "http://localhost:8002/stock/check"


class StockService:
    url = STOCK_URL

    def check_if_all_items_are_available(self, items):
        response = call_api(self.url, {"items": items}).json()
        return response.get("available"), response.get("not_available_items")
