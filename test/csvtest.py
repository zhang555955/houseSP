#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : csvtest.py
# @Author: 橘子
# @Date  : 2020/12/10
# @Desc  : execise
import codecs

import requests
from bs4 import BeautifulSoup
import csv

def db():
    url = "https://www.80s.tw/ju/list"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "Cookie": ''
    }
    ret = requests.get(url, headers=headers)
    return ret.content

#解析网页，并获取帖子的url、标题
def get_data(lst,html_data):
    soup = BeautifulSoup(html_data, "html.parser")
    for i in soup.find_all("a", attrs="title"):
        lst.append([i.attrs["href"], i.attrs["title"]])

#保存url、标题到csv文件中
def save_to_csv(lst):
    with open('testdb.csv', 'w', newline='', encoding='utf-8')as f:
        f = f.write(codecs.BOM_UTF8)
        f_csv = csv.writer(f)
        for data in lst:
            f_csv.writerow(data)



def main():

    Html = db()
    lst = []
    get_data(lst, Html)
    save_to_csv(lst)
main()

