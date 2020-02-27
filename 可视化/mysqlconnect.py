#!/usr/bin/env python
#coding=utf-8
# mysql 数据库连接
#param [p_sql] [可在myslq数据运行的sql代码]
#param [参数2] [参数2说明]
#return [以数组的形式返回sql执行结果]


def db_exec(p_sql):
    # 创建数据库连接
    from pymysql import connect
    # 设置SQL
    tatal_sql = p_sql
    db = connect(host='drdshbga8qzszt6opublic.drds.aliyuncs.com',
                 port=3306,
                 user='its_kf01_workflow',
                 passwd='ServyouITS',
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

testsql="select * from wf_task_target limit 1"
node_info=db_exec(testsql)

for i in range(len(node_info)):
   for j in range(len(node_info[0])):
       print(node_info[i])

