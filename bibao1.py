#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : bibao1.py
# @Author: 橘子
# @Date  : 2020/9/1
# @Desc  : execise

def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of  #返回值是exponent_of函数

square = nth_power(2) #计算一个数的平方
cube = nth_power(3) #计算一个数的立方

print(square(2)) #计算2的平方
print(cube(2)) #计算2的立方