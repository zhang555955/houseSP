#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : openfiletest.py
# @Author: 橘子
# @Date  : 2020/12/10
# @Desc  : execise
import csv

def writeFile(filename,content):
    f = open(filename, "w")
    for i in content:
        f.write(i)
    f.close()

def readFile(filename):
    f = open(filename, "r")
    contents = f.readlines()
    return contents
    f.close()

gushi = ["日照香炉生紫烟\n", "遥看瀑布挂前川\n", "飞流直下三千尺\n", "疑似银河落九天\n"]
writeFile("gushi.csv", gushi)
contents = readFile("gushi.csv")
copy = []
for content in contents:
    copy.append(content)
writeFile("copy.csv", copy)

def writefile(gushi):
    f = open("gushi.csv", "w", encoding='utf-8')
    for i in gushi:
        f.write(i)
        f.write('\n')
    f.close()
def readfile():
     f = open("gushi.csv", "r", encoding='utf-8')
     copy1 = f.readlines()
     f.close()
     f = open("copy.csv", "w", encoding='utf-8')
     for i in copy1:
         f.write(i)
         f.write('\n')
     f.close()
str = ["床前明月光", "疑似地上霜", "举头望明月", "低头思故乡"]
try:
    writefile(str)
    readfile()
except Exception as result:
    print(result)
finally:
    print("结束运行")