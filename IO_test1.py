#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : IO_test1.py
# @Author: 橘子
# @Date  : 2020/8/4
# @Desc  : execise

import re

# """输入input函数"""
# name = input('your name:')
# gender = input('you are a boy?(y/n)')
#
# welcome_str = "welcome to the matrix {prefix}{name}."
# welcome_dic = {
#     'prefix':'Mr.' if gender == 'y' else 'Mrs ',
#     'name':name
# }
#
# print('authorizing...')
# print(welcome_str.format(**welcome_dic))

# """输入input函数"""

def parse(text):

    #用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w]','',text)

    #转为小写
    text = text.lower()

    #生成所有单词的列表
    word_list = text.split(' ')

    #去除空白单词
    word_list = filter(None,word_list)

    #生成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    #按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(),key=lambda kv: kv[1],reverse=True)
    return sorted_word_cnt

with open("E:\\Python36\\test.txt","r") as fin:
    text = fin.read()

word_and_freq = parse(text)

with open ("E:\\Python36\\out.txt","w") as fout:
    for word, freq in word_and_freq:
        fout.write('{}{}\n'.format(word,freq))



