#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : define_vari1.py
# @Author: 橘子
# @Date  : 2020/8/18
# @Desc  : execise

"""def name(param1,param2,param3,...paramN):
    statements
    return/yield value #optional """
#
# def my_sum(a,b):
#     return a + b
# result = my_sum(3,5)
# print(result)

def find_largest_element(l):
    if not isinstance(l,list):
        print('input is not type of list')
        return
    if len(l) == 0:
        print('empty input')
        return
    largest_element = l[0]
    for item in l:
        if item > largest_element:
            largest_element = item
    print('largest element is:{}'.format(largest_element))

find_largest_element([-9,1,-3,2,0])

