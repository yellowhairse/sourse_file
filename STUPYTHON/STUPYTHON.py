#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 15:19
# @Author  : Aries
# @Site    : 
# @File    : STUPYTHON.py
# @Software: PyCharm


#def get_path(path,path_type):
#

def get_filepath(path):
    import os
    filepath = []
    file_path = []
    ot_path = []
    dir_name = os.listdir(path)

    for i in range(len(dir_name)):
        filepath.append(os.getcwd() + '\\' + dir_name[i])

        if os.path.isfile(filepath[i]):
            print(filepath[i])
            file_path.append(filepath[i])
        else:
            ot_path.append(filepath[i])

    return filepath

path = r'C:\Users\wtong\Desktop\DataWorks'

print(get_filepath(path))












