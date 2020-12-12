#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : char_test1.py
# @Author: 橘子
# @Date  : 2020/8/3
# @Desc  : execise

import time


# def query_data(namespace,table):
#     """give 读取某个文件的路径，想要调用数据库API,去读取对应的数据"""
#     path = 'hive://ads/training_table'
#     namespace = path.split('//')[1].split('/')[0]
#     table = path.split('//')[1].split('/')[1]
#     data = query_data(namespace,table)
#
#     print(namespace)

# s = ' my name is jason '
# o = s.rstrip()
# print(o)"""数据处理"""

"""
格式化字符串string.format()
"""
# id = "123"
# name = "jason"
#
# print('no data available for person with id:{},name:{}'.format(id,name))


"""3种遍历字串高效对比"""

start_time = time.perf_counter()
s = ''
for n in range(0,100000):
    s += str(n)
end_time = time.perf_counter()
"""join"""
print('Time elapse1:{}'.format(end_time - start_time))


start_time = time.perf_counter()
l = []
for n in range(0,100000):
    l.append(str(n))
l = ' '.join(l)
end_time = time.perf_counter()
"""join"""
print('Time elapse2:{}'.format(end_time - start_time))

start_time = time.perf_counter()
s = ''.join(map(str,range(0,10000)))
end_time = time.perf_counter()

print('Time elapse3:{}'.format(end_time - start_time))

"""3种遍历字串高效对比"""