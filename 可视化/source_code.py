import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv


def db_exec(p_sql):
    # 创建数据库连接
    import pymysql
    # 设置SQL
    tatal_sql = p_sql
    db = pymysql.connect(host='drdshbga8qzszt6opublic.drds.aliyuncs.com',
                         port=3306,
                         user='its_kf01_workflow',
                         passwd='',
                         database='kf01_workflow',
                         )
    cursors = db.cursor()
    # 执行SQL
    cursors.execute(tatal_sql)
    # 接收查询的数据
    return cursors.fetchall()

    # 关闭连接
    cursors.close()

sql="show tables"
info_sql=db_exec(sql)
for i in range(len(info_sql)):
    print(info_sql[i])

plt.rcParams['font.sans-serif']=['SimHei']   #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False     #用来正常显示负号
from pandas import Series,DataFrame


#Series绘图原理
#指定S的索引
s = pd.Series(np.random.randn(10).cumsum(),#累加
              index=np.arange(0,100,10))
#指定索引
index = np.arange(5)
ax=s.plot(label = "累加折线图",title = "随机累加折线图")

plt.show()


