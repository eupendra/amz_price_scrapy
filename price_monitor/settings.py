# -*- coding: utf-8 -*-

BOT_NAME = 'price_monitor'
SPIDER_MODULES = ['price_monitor.spiders']
NEWSPIDER_MODULE = 'price_monitor.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'price_monitor.pipelines.DBStoragePipeline': 300,
}

AUTOTHROTTLE_ENABLED = True
