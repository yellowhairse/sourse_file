#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/4 15:58
# @Author  : wtong
# @Site    : 
# @File    : get_filename.py
# @Software: PyCharm


path = r'C:\Users\wtong\Desktop\ODPS'


import os

def get_filename(path):

    '''返回目录下所有文件名
    input： [path] [表名头大写]
    outer： [filename]
    例子：get_filename(path)'''

    file_name = []
    folder_name = []
    list = os.listdir(path)

    for i in range(len(list)):
        list[i] = path+'\\'+list[i]
        if os.path.isdir(list[i]):
            folder_name.append(list[i])
        else:
            file_name.append(list[i])

    return file_name

def get_foldername(path):

    '''返回目录下所有文件夹名称
    input： [path] [表名头大写]
    outer： [foldername]
    例子：get_foldername(path)'''

    path1 = path

    def get_foldername_local(path1):
        file_name = []
        folder_name = []
        list = os.listdir(path1)

        for i in range(len(list)):
            list[i] = path1 + '\\' + list[i]
            if os.path.isdir(list[i]):
                folder_name.append(list[i])
            else:
                file_name.append(list[i])

        return folder_name

    while  get_foldername_local(path)



print(get_foldername(path))







