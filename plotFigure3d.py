# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def readData(file_path):
    # 打开一个文本文件
    text_file = open(file_path)
    data_item = []
    # 垂轨数据
    xy_ev = []
    # 沿轨数据
    xy_eh = []

    # 先读取第一行，读取时注意去掉行尾的换行符
    line = text_file.readline().strip('\n')
    # 然后逐行读取数据
    while line:
        line = text_file.readline().strip('\n')
        # 如果读取的行内容不为空，则添加到list中
        # 注意这里并不能用None，注意空字符串和空对象的区别
        if line != '':
            data_item.append(line)

    # 读取完成后对于读取的每行数据进行简单的提取和处理
    for i in range(data_item.__len__()):
        data = data_item[i].split('\t')
        x_coordinate = float(data[1])
        y_coordinate = float(data[2])
        error_vertical = float(data[5])
        error_horizontal = float(data[6])
        xy_ev.append([x_coordinate, y_coordinate, error_vertical])
        xy_eh.append([x_coordinate, y_coordinate, error_horizontal])

    return xy_ev, xy_eh


print("Reading data...")
xy_ev, xy_eh = readData("SC_Accuracy_Ru.txt")
print("Read data success.")

xy_ev_new = []
xy_eh_new = []
for i in range(0, xy_ev.__len__(), 30):
    xy_ev_new.append(xy_ev[i])
    xy_eh_new.append(xy_eh[i])

ax = plt.subplot(111, projection='3d')
ax.scatter(np.array(xy_eh_new)[:, 0], np.array(xy_eh_new)[:, 1], np.array(xy_eh_new)[:, 2], c='r')
ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()

ax = plt.subplot(111, projection='3d')
ax.scatter(np.array(xy_ev_new)[:, 0], np.array(xy_ev_new)[:, 1], np.array(xy_ev_new)[:, 2], c='b')
ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()
