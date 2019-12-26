#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 20:07
# @Author  : Aries
# @Site    : 
# @File    : 文件目录结构.py
# @Software: PyCharm


def get_filename(path):
    import os
    filepath=[]
    ot_path =[]
    dir_name=os.listdir(path)
    for i in range(len(dir_name)):
        filepath.append(os.getcwd() + '\\' + dir_name[i])
        if os.path.isfile(filepath[i]):
            print(filepath[i])




a='C:\\Users\\wtong\\Documents\\王彤\\数据可视化课题\\sourse_file'
print(get_filename(a))

