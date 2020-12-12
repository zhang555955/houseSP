#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : define_vari2.py
# @Author: 橘子
# @Date  : 2020/8/31
# @Desc  : execise

def factorial(input):
    #validation check
    if not isinstance(input,int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0')
    ...

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input-1)
    return inner_factorial(input)

print(factorial(-5))
