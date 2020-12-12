#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : testRE.py
# @Author: 橘子
# @Date  : 2020/12/7
# @Desc  : execise

#正则表达式：字符串模式，判断字符串附合一定的标准
import re
#创建模式对象

pat = re.compile("AA")      #此处的AA是正则表达式，用来验证其它的字符串。标准
# m = pat.search("CBA,")      #search字符串后面的内容，被检验的内容。
# m = pat.search("ABCAA")
# m = pat.search("ABCAADDCCAAA")

#没有模式对象

# m = re.search("asd","Aasd")     #前面字符串是规则模版，后边是被检验的。
# print(m)

# print(re.findall("[A-Z]", "ASDaDFGAa"))      #前面字符串是规则模版(正则表达式)，后边是被检验的。
# print(re.findall("[A-Z]+", "ASDaDFGAa"))      #前面字符串是规则模版(正则表达式)，后边是被检验的。

#sub

# print(re.sub("a","A","abcdcasd"))       #找到小a替换成大A，在第3个的字符串里。

#建议在正则表达式中，被比较的字符串前面加上r,不用担心转译字符的问题。
a = r"\aabd-\'"
print(a)