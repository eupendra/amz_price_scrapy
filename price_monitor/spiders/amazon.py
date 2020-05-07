import json
import pkgutil
from datetime import datetime

import scrapy

from ..items import PriceMonitorItem
from ..utils import amazon_headers


class AmazonSpider(scrapy.Spider):
    name = "amazon"

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': amazon_headers
    }

    def start_requests(self):
        products = json.loads(pkgutil.get_data('price_monitor', 'resources/products.json').decode())
        for name, urls in products.items():
            for url in urls:
                if self.name in url:
                    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                    item = PriceMonitorItem(product_name=name, when=now)
                    yield scrapy.Request(url, meta={'item': item})

    def parse(self, response):
        # inspect_response(response, self)
        item = response.meta.get('item', PriceMonitorItem())
        item['url'] = response.url
        item['title'] = response.css("span#productTitle::text").get().strip()
        if response.css("span#priceblock_dealprice::text"):
            item['deal_price'] = float(
                response.css("span#priceblock_dealprice::text").re_first(r"[\d,.]+").replace(',', '') or -1
            )
            item['deal'] = True
        else:
            item['deal'] = False
            item['deal_price'] = -1
        if response.css("span#priceblock_ourprice"):
            item['regular_price'] = float(
                response.css("span#priceblock_ourprice::text").re_first(r"[\d,.]+").replace(',', '') or -1
            )
        else:
            item['regular_price'] = -1
        yield item
