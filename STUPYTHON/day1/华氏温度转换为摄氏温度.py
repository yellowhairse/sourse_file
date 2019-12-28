#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/28 11:27
# @Author  : wtong
# @Site    : 
# @File    : 华氏温度转换为摄氏温度.py
# @Software: PyCharm

#华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$


F = float(input("华氏温度为："))

print("摄氏温度为%.2f" % ((F - 32)/1.8))
