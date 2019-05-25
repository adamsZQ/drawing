
acc_list = []
with open('loss','r') as f:
    for line in f:
        if 'accuracy' in line:
            acc_list.append(float(line[10:16]))

print(acc_list)



import numpy as np
import matplotlib.pyplot as plt
#X轴，Y轴数据
x = [a for a in range(len(acc_list))]
y = acc_list
# plt.figure(figsize=(8,4)) #创建绘图对象
plt.plot(x,y,marker='o')   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.xlabel("Time(s)") #X轴标签
plt.ylabel("Volt")  #Y轴标签
plt.title("") #图标题
plt.show()  #显示图

