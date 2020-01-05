#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/4 15:58
# @Author  : wtong
# @Site    : 
# @File    : get_filename.py
# @Software: PyCharm

import os

def get_filename(path):

    '''返回目录下所有文件名
    input： [path] [表名头大写]
    outer： [filename]
    sample：get_filename(path)'''

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
    sample：get_foldername(path)'''

    dir_name = list()
    dir_name.append(path)
    st_idx = 0
    ed_idx = 1

    def get_foldername_local(path):
        file_name = []
        folder_name = []
        list = os.listdir(path)

        for i in range(len(list)):
            list[i] = path + '\\' + list[i]
            if os.path.isdir(list[i]):
                folder_name.append(list[i])
            else:
                file_name.append(list[i])
        return folder_name

    while st_idx < ed_idx:
        for i in dir_name[st_idx:ed_idx]:
            for j in get_foldername_local(i):
                dir_name.append(j)
        st_idx = ed_idx
        ed_idx = len(dir_name)

    return dir_name

path = r'C:\Users\wtong\Desktop'

for i in get_filename(path):
    print(i)
