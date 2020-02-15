# coding=utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager
import random


"""
matplotlib 默认不支持中文字符

"""
#windws和linux设置字体的方式
# font = {'family' : 'SIMYOU.TTF',
#         'weight': 'bold',
#         'size': 'larger'}
# font_manager.rc("font",**font)
# font_manager.rc("font",family='SIMYOU.TTF',weight="bold")

#另外一种设置字体的方式
font = font_manager.FontProperties(fname="test.ttf")

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

#调整x轴的刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
#取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=font) #rotaion旋转的度数
# plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=90)

#添加描述信息
# plt.xlabel("时间",fontproperties=font)
# plt.ylabel("温度 单位(℃)",fontproperties=font)
# plt.title("10点到12点每分钟的气温变化情况",fontproperties=font)

plt.show()