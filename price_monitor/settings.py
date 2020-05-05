# -*- coding: utf-8 -*-

BOT_NAME = 'price_monitor'
SPIDER_MODULES = ['price_monitor.spiders']
NEWSPIDER_MODULE = 'price_monitor.spiders'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'price_monitor.pipelines.CSVStoragePipeline': 300,
}

AUTOTHROTTLE_ENABLED = False
