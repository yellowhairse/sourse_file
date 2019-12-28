#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 20:07
# @Author  : Aries
# @Site    : 
# @File    : 文件目录结构.py
# @Software: PyCharm


#coding=utf-8
# 查找目录结构下文件和文件夹名称
#param [path] [路径]
#param [num] [1 为文件，0 为 文件夹]
#return [以数组的形式返回sql执行结果]

def get_path(path,num):
    import os
    filepath = []
    file_path = []
    ot_path = []
    dir_name = os.listdir(path)
    for i in range(len(dir_name)):
        filepath.append(os.getcwd() + '\\' + dir_name[i])
        if os.path.isfile(filepath[i]):
            file_path.append(filepath[i])
        else:
            ot_path.append(filepath[i])
    if num:
        return file_path
    else:
        return ot_path



path = r'C:\Users\wtong\Desktop\DataWorks'
t = get_path(path,1)
print(t)

