import json
import pkgutil
from datetime import datetime, timedelta


def timestamp_from_reversed(reversed):
    return datetime(5000, 1, 1) - timedelta(seconds=float(reversed))


def reversed_timestamp():
    return str((datetime(5000, 1, 1) - datetime.now()).total_seconds())


def normalize_name(name):
    return name.replace('-', '')


def get_product_names():
    return [
        normalize_name(name)
        for name in json.loads(
            pkgutil.get_data("price_monitor", "resources/products.json").decode()
        ).keys()
    ]


def get_retailer_name_from_url(url):
        return url.split("://")[1].split("/")[0].replace("www.", "")


def get_retailers_for_product(product_name):
    data = json.loads(
        pkgutil.get_data("price_monitor", "resources/products.json").decode()
    )
    return {get_retailer_name_from_url(url) for url in data[product_name]}


amazon_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8,hi;q=0.7',
    'cache-control': 'max-age=0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/81.0.4044.129 Safari/537.36 '
}
