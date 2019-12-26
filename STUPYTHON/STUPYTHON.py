#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 15:19
# @Author  : Aries
# @Site    : 
# @File    : STUPYTHON.py
# @Software: PyCharm


import os

path=r'C:\Users\wtong\Documents\王彤\数据可视化课题\sourse_file'

import os

filepath = []
ot_path = []
dir_name = os.listdir(path)
for i in range(len(dir_name)):
    filepath.append(os.getcwd() + '\\' + dir_name[i])
print(filepath[0])

print(os.path.isdir(filepath[0]))

    flag=os.path.isfile(filepath[i])
    print(flag)

    if os.path.isdir(filepath[i]):
        print(filepath[i])


