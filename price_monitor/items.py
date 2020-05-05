# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PriceMonitorItem(scrapy.Item):
    product_name = scrapy.Field()
    title = scrapy.Field()
    deal = scrapy.Field()
    deal_price = scrapy.Field()
    regular_price = scrapy.Field()
    when = scrapy.Field()
    url = scrapy.Field()
