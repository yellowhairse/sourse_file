#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/4 15:58
# @Author  : wtong
# @Site    : 
# @File    : get_filename.py
# @Software: PyCharm

import os

def get_new_report(filepath):
    '''返回目录下创建时间最新的文件的名称
     input： [filepath] [路径]
     outer： [filename]
     sample：get_filename(path)'''
    lists = os.listdir(filepath)  #列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn:os.path.getmtime(filepath + "\\" + fn))  # 按时间排序
    filename = os.path.join(filepath,lists[-1])  # 获取最新的文件保存到file_new
    return filename


def get_listname(path,flag):

    '''返回目录下所有文件名
    input： [path] [路径]
            [flag] [返回类型: F 文件 D 目录]
    outer： [filename]
    sample：get_filename(path)'''

    file_name = []
    folder_name = []
    err_code = '您输入的返回类型不符合要求',
    list = os.listdir(path)

    for i in range(len(list)):
        list[i] = path+'\\'+list[i]
        if os.path.isdir(list[i]):
            folder_name.append(list[i])
        else:
            file_name.append(list[i])

    if flag == 'F':
        return file_name
    elif flag == 'D':
        return folder_name
    else:
        return err_code


def get_everylistname(path):

    '''返回目录下所有文件夹名称
    input： [path] [表名头大写]
    outer： [foldername]
    sample：get_foldername(path)'''

    dir_name = list()
    dir_name.append(path)
    GlobalValue =(0,1)
    st_idx , ed_idx = GlobalValue

    while st_idx < ed_idx:
        for i in dir_name[st_idx:ed_idx]:
            for j in get_listname(i,'D'):
                dir_name.append(j)
        st_idx = ed_idx
        ed_idx = len(dir_name)

    return dir_name

path = r'E:\SVN\资料文件\MX_ZRRYH_CXTJ\codes'

get_listname(path,'D')
# filename = []
# for i in get_everylistname(path):
#
#     filename.extend(get_listname(i,'F'))
#
# for j in filename:
#     print(j)

