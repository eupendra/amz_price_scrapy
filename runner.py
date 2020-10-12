#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import matplotlib.pyplot as plt
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import config
from db_helper import get_df_from_db


def run_crawler():
    process = CrawlerProcess(get_project_settings())

    process.crawl('amazon')
    process.start()


def send_mail(body, subject):
    import smtplib
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = config.USER_NAME
    msg['To'] = config.USER_NAME
    text = "Scraped today's prices"
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(body, 'html')
    msg.attach(part1)
    msg.attach(part2)
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(config.USER_NAME, config.USER_PASS)
    smtp.sendmail(config.USER_NAME, config.USER_NAME, msg.as_string())
    smtp.quit()


def get_csv_contents():
    import csv
    output = '<table border=1>'
    with open('amazon.csv', 'r') as f:
        for row in list(csv.reader(f))[:1]:
            output += '<tr>'
            for cell in row:
                output += '<th>'
                output += cell
                output += '</th>'
            output += '</tr>\n'
    with open('amazon.csv', 'r') as f:
        for i, row in enumerate(reversed(list(csv.reader(f)))):
            output += '<tr>'
            for cell in row:
                output += '<td>'
                if 'True' in str(cell):
                    output += '<b>YES</b>'
                elif 'False' in str(cell):
                    output += '<i>No<i>'
                else:
                    output += cell
                output += '</td>'
            output += '</tr>\n'
            if i == 10:
                break
    return output + '</table>'


def get_mail_body(dataframe):
    df = dataframe.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # strip whitespace
    asins = set(df['asin'].tolist())
    dfs = []
    for asin in asins:
        dfs.append(df[df['asin'] == asin][['asin', 'regular_price', 'ts']])
    for d in dfs:
        plt.plot(d['regular_price'], x='ts')
        plt.show()


if __name__ == '__main__':
    print('Running Spider')
    run_crawler()
    print('Reading historical Data')
    df = get_df_from_db()
    # body = get_mail_body(df)
    print('Sending mail')
    send_mail(df.to_html(classes='table table-striped'), f"Today's prices from Pi - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print('Done')
