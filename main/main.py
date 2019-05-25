
acc_list = []
f_list = []

with open('pretrain_loss','r') as f:
    for line in f:
        if 'accuracy' in line:
            acc_list.append(float(line[10:16]))
            f_list.append(float(line[57:63]))

print(acc_list)
print(f_list)



import numpy as np
import matplotlib.pyplot as plt
#X轴，Y轴数据
x = [a for a in range(len(acc_list))]
y = acc_list
# plt.figure(figsize=(8,4)) #创建绘图对象
plt.plot(x,y,marker='o', mec='b', label='Accuracy')   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.plot(x,f_list, marker='o', mec='r', label='F1')   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）

plt.xlabel("Epoch") #X轴标签
# plt.ylabel("Accuracy")  #Y轴标签
# plt.title("预训练准确率结果统计") #图标题
plt.legend() # 显示图例

plt.show()  #显示图

