# -*- coding: utf-8 -*-
import csv
import sqlite3
from os import path

from db_helper import create_table, insert_item


class CSVStoragePipeline(object):

    def __init__(self):
        file_exists = path.exists('amazon.csv')
        self.file = open('amazon.csv', 'a', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, fieldnames=[
            'product_name', 'title', 'deal', 'price', 'when', 'url'
        ])
        if not file_exists:
            self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()


class DBStoragePipeline(object):

    def __init__(self):
        self.conn = sqlite3.connect("amazon.db")
        self.cur = self.conn.cursor()
        create_table(self.cur)

    def process_item(self, item, spider):
        print('in process items')
        insert_item(self.cur, self.conn, item)
        return item

    def __del__(self):
        print('Closing Connection...')
        self.conn.close()
