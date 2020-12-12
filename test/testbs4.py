#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : testbs4.py
# @Author: 橘子
# @Date  : 2020/12/3
# @Desc  : execise
import re

from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")

#css选择器

# t_list = bs.select('title')   #通过标签来查找
# t_list = bs.select(".mnav")     #通过类名查找
# t_list = bs.select("#u1")       #通过ID来查找
# t_list = bs.select("a[class='s-set-skin']")       #通过属性来查找
#t_list = bs.select("head > title")       #通过子标签来查找
#t_list = bs.select("head > title")       #通过子标签来查找，兄弟节点标签

t_list = bs.select("title")
print(t_list[0].get_text())

# for item in t_list:
#     print(item)

#方法：传入一个函数（方法），根据函数的要求搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)

#kwargs 参数

# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)
#
# for item in t_list:
#     print(item)

#3.text参数
#t_list = bs.find_all(text = "hao123")
# t_list = bs.find_all(text=["hao123","地图","贴吧"])
#4.limit 参数
# t_list = bs.find_all(text=re.compile("\d"))   #应用正则表达式来查找包含指定文本的内容（标签里的字符串）




# print(bs.title)
# print(bs.a)
# print(type(bs.head))
#1.Tag  标签及其内容：拿到它所找到的第一个内容

# print(bs.title.string)

# print(bs.a.attrs)
#2.NavigableString  标签里的内容（字符串）


#3.BeautifulSoup  表示整个文档

# print(bs)

#4.comment 是一个特殊的NavigableString，输出的内容不包含注释符号
# print(bs.a.string)

#---------------------------------------------

#文档遍历

# print(bs.head.contents)

#文档的搜索
#1.字符窜过滤，
# t_list = bs.find_all("a")

#2.正则表达式搜索：使用search()方法匹配内容
# t_list = bs.find_all(re.compile("a"))

#3.方法：传入一个函数（方法），根据函数的要求搜索

# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
# print(t_list)


