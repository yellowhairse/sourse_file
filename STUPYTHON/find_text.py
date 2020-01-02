#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 15:54
# @Author  : wtong
# @Site    : 
# @File    : find_text.py
# @Software: PyCharm


import os

#coding=utf-8
# 提取文件内sql 的表明（输入表名称的开头）
#param [find_str] [表名头大写]
#param [file_path] [文件路径]
#param [filename] [文件名称]
#return [表名]
#f_find_text('DIM',file_path,filename)

def f_find_text(find_str,file_path,filename):

    os.chdir(file_path)
    f = open(filename,encoding='utf-8')
    name = []
    disname = []

    f_read = f.readlines()

    for i in range(len(f_read)):
        t_line = f_read[i]
        sta_index = t_line.find(find_str)
        end_index = t_line.find(' ',sta_index)
        if t_line[sta_index:end_index] in '':
            pass
        else:
            name.append(t_line[sta_index:end_index])

    f.close()

    for i in range(len(name)):
        if name[i] not in disname:
            disname.append(name[i])

    return disname


file_path = r"C:\Users\wtong\Desktop\work\其他"
filename = r'test.txt'

l_name = ['DIM','F_BT','F_RT']

table_name = []

for i in range(len(l_name)):
    table_name.append(f_find_text(l_name[i], file_path, filename))

print(table_name)

