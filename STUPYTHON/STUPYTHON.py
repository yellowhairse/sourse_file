#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 15:19
# @Author  : Aries
# @Site    : 
# @File    : STUPYTHON.py
# @Software: PyCharm


def get_path(path,path_type):
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

    if path_type:
        return file_path
    else:
        return ot_path




path = r'C:\Users\wtong\Documents\王彤\数据可视化课题\sourse_file'
t = get_path('1',0)
print(t)

