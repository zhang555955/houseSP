#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : except_test1.py
# @Author: 橘子
# @Date  : 2020/8/11
# @Desc  : execise
#
# try:
#     s = input('please enter two numbers separated by comma:')
#     num1 = int(s.split(',')[0].strip())
#     num2 = int(s.split(',')[1].strip())
# except ValueError as err:
#     print('Value Erro:{}'.format(err))
# except IndexError as err:
#     print('Index Erro:{}'.format(err))
# except Exception as err:  #也可以省略异常类型except:
#     print('other Erro:{}'.format(err))
#
# print('continue')


# import sys
# try:
#     f = open('test.txt','r')
# except OSError as err:
#     print('OS error:{}'.format(err))
# except:
#     print('Unexpected error:',sys.exc_info()[0])
# finally:
#     f.close()
#"""异常"""

# """自定义异常"""
#
# class MyInputError(Exception):
#     """输入错误时"""
#     def __init__(self,value): #自定义异常类型的初始化
#         self.value = value
#     def __str__(self): #自定义异常类型string表达式
#         return ("{} is invalid input".format(repr(self.value)))
#
# try:
#     raise MyInputError(1) #抛出MyInputError这个异常
# except MyInputError as err:
#     print('error:{}'.format(err))

import json
try:
    data = json.loads(raw_data)
    ...
except JSPNDecodeError as err:
    print('JSONDecodeError:{}'.format(err))