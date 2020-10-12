import sqlite3
from os import path, getcwd
import pandas as pd


def create_table(cur):
    sql = '''
                create table if not exists items(
                    asin text,
                    product_name text,
                    title text,
                    deal text,
                    price text,
                    url text,
                    ts timestamp
                )
            '''
    cur.execute(sql)


def insert_item(cur, conn, item):
    sql = ' insert into items (asin,product_name,title,deal,price,url,ts) ' \
          ' values (?,?,?,?,?,?,?) '
    cur.execute(sql,
                (
                    item['asin'],
                    item['product_name'],
                    item['title'],
                    item['deal'],
                    item['price'],
                    item['url'],
                    item['ts']
                )
                )
    conn.commit()


def execute_sql(sql, cur, conn):
    cur.execute(sql)
    conn.commit()


def get_df_from_db():
    db_file = path.join(getcwd(), "amazon.db")
    if not path.exists(db_file):
        return None
    conn = sqlite3.connect(db_file)

    df = pd.read_sql_query("select * from items", conn)
    conn.close()

    return df

    # conn = sqlite3.connect("amazon.db")
    # get_asin_sql = 'select DISTINCT(asin) from items'
    # conn.row_factory = sqlite3.Row
    # cursor = conn.cursor()
    # cursor.execute(get_asin_sql)
    #
    # asins = list()
    # for r in cursor.fetchall():
    #     for c in r:
    #         asins.append(c)
    #
    # print(asins)
    #
    # sql_select_asin_history = '''
    #        select
    #            asin,
    #            product_name,
    #            title,deal,
    #            deal_price,
    #            regular_price,
    #            url,
    #            ts as `time`
    #
    #            from items
    #
    #            where asin ={}
    #
    #            order by ts desc
    #            limit 10
    #     '''
    #
    # conn.row_factory = sqlite3.Row
    # cursor = conn.cursor()
    # cursor.execute(sql_select_asin_history)
    # table = []
    # for r in cursor.fetchall():
    #     row = list()
    #     for c in r:
    #         row.append(c)
    #     table.append(row)
    # headers = [x[0] for x in cursor.description]
    # return tabulate(table, headers, tablefmt="html")
