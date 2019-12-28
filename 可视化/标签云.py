#!/usr/bin/env python

import pymysql
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
import time
import os

#coding=utf-8
# mysql 数据库连接
#param [p_sql] [可在myslq数据运行的sql代码]
#param [参数2] [参数2说明]
#return [以数组的形式返回sql执行结果]
def db_exec(p_sql):
    # 创建数据库连接
    # 设置SQL
    tatal_sql = p_sql
    db = pymysql.connect(host='drdshbga8qzszt6opublic.drds.aliyuncs.com',
                         port=3306,
                         user='its_kf01_workflow',
                         passwd='SerITS',
                         database='kf01_workflow',
                         )
    cursors = db.cursor()
    # 执行SQL
    cursors.execute(tatal_sql)
    # 接收查询的数据
    return_info = cursors.fetchall()
    return return_info
    # 关闭连接
    cursors.close()

#coding=utf-8
# 标签云可视化控件
#param [p_words] [要进行展示的信息]
#param [p_title] [界面标题]
#param [p_html_path] [生产html文件的路径]
#param [p_html_name] [生产html文件的名称]
#return [html文件]
#wordcloud_base(words,'标签','C:\\Users\\wtong\\Desktop','标签云')

def wordcloud_base(p_words,p_title,p_html_path,p_html_name) -> WordCloud:
    local_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    c = (
        WordCloud()
        .add("", p_words, word_size_range=[20, 100])
        .set_global_opts(title_opts=opts.TitleOpts(title=local_time+'  '+p_title))
    )
    len_path=len(p_html_path)
    if len_path==0:
        t = os.path.exists('C:\\dataview')
        if t:
            os.chdir('C:\\dataview')
        else:
            os.mkdir('C:\\dataview')
            os.chdir('C:\\dataview')
    else:
        os.chdir(p_html_path)
    return c.render(p_html_name+'.html')



#定义要执行的sql 语句
exec_sql=''' 
select
replace(replace(swjg.SWJGMC,'国家税务总局',''),'税务局',''),count(1)*10
from wf_process_define wf
inner join dm_gy_swjg swjg on wf.CREATE_DEPT=swjg.swjg_dm
group by swjg.SWJGMC
order by count(1) desc 
limit 20  ; '''
node_info=db_exec(exec_sql)

#定义空列表
list1=[]
#循环取值拼接为列表
for i in range(len(node_info)):
    #print(node_info[i])
    str=(node_info[i])
    list1.append(str)

#对象重命名
list_info=list1

#print(list_info)

#生成html文件
wordcloud_base(list_info,'标签','','标签云')
#打开html文件
import webbrowser

filename = 'file:///C:/dataview/' + '标签云.html'
webbrowser.open_new_tab(filename)

