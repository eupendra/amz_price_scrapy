# -*- coding: utf-8 -*-
import csv


class CSVStoragePipeline(object):

    def __init__(self):
        self.file = open('amazon.csv', 'a', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, fieldnames=[
            'product_name', 'title', 'deal', 'deal_price', 'regular_price', 'when', 'url'

        ])

    def process_item(self, item, spider):
        self.writer.writeheader()
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()
