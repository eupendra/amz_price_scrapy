# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PriceMonitorItem(scrapy.Item):
    asin = scrapy.Field()
    product_name = scrapy.Field()
    title = scrapy.Field()
    deal = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    ts = scrapy.Field()
