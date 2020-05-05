# -*- coding: utf-8 -*-
import csv
from os import path


class CSVStoragePipeline(object):

    def __init__(self):
        file_exists = path.exists('amazon.csv')
        self.file = open('amazon.csv', 'a', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, fieldnames=[
            'product_name', 'title', 'deal', 'deal_price', 'regular_price', 'when', 'url'
        ])
        if not file_exists:
            self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()
