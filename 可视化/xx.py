import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=['SimHei']  # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示负号

#再论柱状图
#创建一个画板
plt.figure(1)
# 确定绘图范围，由于只需要画一张图，所以我们将整张白纸作为绘图的范围
# 111: 表示设置绘图范围为1行1列，最后一个1代输出到第1块画布上目前只有1块）
ax1=plt.subplot(111)

#数据准备
#y轴数据
data = np.array([15,10,25,15,7])
width=0.8#柱状图宽度
#x轴数据
x_bar = np.arange(5)
rect=ax1.bar(x_bar,data,width=width,color="lightblue")
#为柱状图添加高度值
for rec in rect:
    x=rec.get_x() #获取所有x坐标的值
    height=rec.get_height()  #获取所在高度的值
    print(x,height)
    ax1.text(x+0.2,1.02*height,str(height)+'W')  #在指定位置写上高度的值
#设置x的坐标
ax1.set_xticks(x_bar)
ax1.set_xticklabels(["第一季度","第二季度","第三季度","第四季度"])
ax1.set_xlabel("季度")
#设置Y的标签
ax1.set_ylabel("销量(单位:万件)")
ax1.set_title("2017年季度销售量统计")
ax1.grid(True)  #是否显示网格
ax1.set_ylim(0,28) #设置y的显示范围


ax1.spines["right"].set_color("none")
ax1.spines["top"].set_color("none")

plt.show()