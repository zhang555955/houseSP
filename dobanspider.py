#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : dobanspider.py
# @Author: 橘子
# @Date  : 2020/11/27
# @Desc  : execise

import urllib.error  # 得到网页即可
from urllib import request

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字 匹配
import xlwt  # 进行execl操作
import sqlite3  # 进行SQLLite数据库操作
from lxml import etree
from time import sleep

num = 0

findlink = re.compile(r'<a href="(.*?)">')     #生成创建正则表达式对象，表示规则（字符串模式）
url = "https://www.80s.tw"
def getData(url):

    # refer = "https://www.80s.tw"
    headers = {
        # "Referer": refer,
        "User-Agent": "user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    # html = etree.HTML(content)
    print(html)

    # soup = BeautifulSoup(html, "html.parser")
    # for item in soup.find_all('div', class_="clearfix noborder block1"):
    #     data = []
    #     item = str(item)
    #     link = re.findall(findLink, item)[0]     #re库用来通过正则表达式查找指定的字符串
    #
    #     print(data)
    #     print(link)

    # user = html.xpath('//div[@class="brokerInfoText"]')[0]
    #
    # name = user.xpath('div[@class="brokerName"]/a')[0].text
    # pf = user.xpath('div[@class="evaluate"]/span')[0].text
    # num = user.xpath('div[@class="evaluate"]/span')[1].text

    # print(name)
    # print(pf.strip())
    # print(num)
    # return name,pf.strip(),num

# def getHouse(url, refer):
#     global num
#     headers = {
#         "Referer": refer,
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
#     }
#
#     req = request.Request(url, headers=headers)
#
#     response = request.urlopen(req)
#
#     content = response.read().decode()
#
#     html = etree.HTML(content)
#
#     house_list = html.xpath('//ul[@id="house-lst"]/li/div[@class="info-panel"]/h2/a')
#     for house in house_list:
#         attrib = house.attrib
#         housename = attrib["title"]
#         houseurl = attrib["href"]
#         print("%s : %s" % (housename, houseurl))
#         print("%s 开始爬取"%housename)
#         name, pf, Num = getUser(houseurl,url)
#         print("%s 爬取结束"%housename)
#         sleep(1)
#         num += 1
#         h = House()
#         h.houseName = housename
#         h.houseUrl = houseurl
#         h.houseUser = name
#         h.userPF = pf
#         h.lookNum = Num
#         h.save()
#
#
# if __name__ == "__main__":
#     for i in range(1, 3):
#         if i == 1:
#             url = "https://www.80s.tw/ju/list"
#             refer = "https://www.80s.tw"
#         else:
#             refernum = i - 1
#             url = "https://www.80s.tw/ju/list/----0--p/%s/" % i
#             refer = "https://www.80s.tw/ju/list/----0--p/%s/" % refernum
#         print("第 %s 页开始爬取" % i)
#         # getHouse(url, refer)
#         sleep(1)
#         print("第 %s 页爬取结束" % i)
#     print(num)



# def main():
#     url = "https://www.80s.tw"
#     datalist = getData(url)


    # savespath = ".\\电影80.xls"
    # saveData(savepath)




# def askURl(url):
#     head = {
#         "user-agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
#     }
#
#     request = urllib.request.Request(url, headers=head)
#     html = ""
#
#     try:
#         response = urllib.request.urlopen(request)
#         html = response.read().decode("utf-8")
#         print(html)
#
#     except urllib.error.URLError as e:
#         if hasattr(e, "code"):
#             print(e.code)
#         if hasattr(e, "reason"):
#             print(e.reason)
#     return html
#
# def getData(baseurl):
#     datalist = []
#     for i in range(0, 10):
#         url = baseurl
#         html = askURL(url)
#
#         soup = BeautifulSoup("html.parser")
#     return datalist
#
# def saveData(savepath):
#
#     saveData("save....")
#
#
#
# if __name__ == "__main__":
#     baseurl = "https://www.80s.tw/ju/list"
#     url = "baseurl"+"/"+"----0--p/"+"i"
#
#     datalist = getData(baseurl)
#     print(datalist)
#
