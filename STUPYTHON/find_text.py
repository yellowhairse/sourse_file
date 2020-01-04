#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 15:54
# @Author  : wtong
# @Site    : 
# @File    : find_text.py
# @Software: PyCharm
#coding = utf - 8

import os

def f_find_text(find_str,file_path,filename):

    '''提取文件内sql 的表明（输入表名称的开头）
    input：param [find_str] [表名头大写]
           param [file_path] [文件路径]
           param [filename] [文件名称]
    outer：return [表名]
    例子：f_find_text('DIM',file_path,filename)'''
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
        else:
            pass

    return disname

#
# file_path = r"C:\Users\wtong\Desktop\work\其他\复杂重点清册清单"
# filename = ['个人所得税应申报清册.txt','净入库.txt','征收开票.txt']
#
# l_name = ['DIM','F_BT','F_RT']
#
# temp_tab = []
# tab_name = []
#
# for i in range(len(l_name)):
#     for j in range(len(filename)):
#         temp_tab.extend(f_find_text(l_name[i], file_path, filename[j]))
#
# for i in range(len(temp_tab)):
#     if temp_tab[i] not in tab_name:
#         tab_name.append(temp_tab[i])
#     else:
#         pass
#
#
# print(tab_name)
#
# help(f_find_text)