#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : testUrllib.py
# @Author: 橘子
# @Date  : 2020/11/30
# @Desc  : execise
import codecs
import re
import urllib.request
import ssl
from time import sleep
import csv
import openpyxl

from lxml import etree

from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context

def getURL(url,refer):

    headers = {
        "Referer": refer,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    ul = soup.find_all('ul', class_='me1 clearfix')
    
    # 重新格式目标串
    li = []
    li.extend(ul[0].find_all('li'))

    
    for l in li:
        Mtitle = l.attrs['title']
        Mlink = l.attrs["href"]
        Mphoto = l.img["src"]

        lst

        with open('tieba_title.csv', 'ab+') as f1:
            f1.write(codecs.BOM_UTF8)
        #
        # with open('tieba_title.csv', 'a+', encoding='utf-8', errors='ignore', newline="") as f2:
        #     writer = csv.Writer(f)
        #     writer.writerow('表头列表')
        #     writer.writerow('每一行信息组成的列表')

        with open('test.csv', 'w', newline='', encoding='utf-8') as f:
            f_csv = csv.writer(f)
            for lst in li:
                f_csv.writerow(lst)




if __name__ == "__main__":

    for i in range(1, 3):
        if i == 1:
            url = "https://www.80s.tw/ju/list"
            refer = "https://www.80s.tw"
        else:
            refernum = i - 1
            url = "https://www.80s.tw/ju/list/----0--p/%s" % i
            refer = "https://www.80s.tw/ju/list/----0--p/%s" % refernum
        print("第 %s 页开始爬取" % i)
        getURL(url, refer)

        print("第 %s 页爬取结束" % i)
        print("=====" * 30)
        sleep(1)
        
