# coding=utf-8
from matplotlib import pyplot as plt
import numpy as np


def readData(file_path):
    # 打开一个文本文件
    text_file = open(file_path)
    data_item = []
    # x轴垂轨数据
    x_ev = []
    # x轴沿轨数据
    x_eh = []
    # y轴垂轨数据
    y_ev = []
    # y轴沿轨数据
    y_eh = []

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
        x_ev.append([x_coordinate, error_vertical])
        x_eh.append([x_coordinate, error_horizontal])
        y_ev.append([y_coordinate, error_vertical])
        y_eh.append([y_coordinate, error_horizontal])

    # 由于原始数据中坐标并没有进行排序，因此这里进行排序
    x_ev.sort()
    x_eh.sort()
    y_eh.sort()
    y_ev.sort()
    return x_ev, x_eh, y_ev, y_eh


file_path = "SC_Accuracy_Ru.txt"
x_ev, x_eh, y_ev, y_eh = readData(file_path)

# 设置绘图的大小(格网)
plt.figure(figsize=(16, 10))

# 221表示分成2行2列，占用第一块(1行1列)
plt.subplot(221)
plt.title("Rule of residual errors across the track")
plt.xlabel("X")
plt.ylabel("Errors(pixels)")
plt.grid(True)
# s表示散点大小，alpha表示透明度，c表示颜色
points = plt.scatter(np.array(x_ev)[:, 0],
                     np.array(x_ev)[:, 1],
                     s=1,
                     alpha=0.5,
                     c='r')
plt.legend([points], ['Across Track Error'])

# 221表示分成2行2列，占用第三块(2行1列)
plt.subplot(223)
plt.title("Rule of residual errors along the track")
plt.xlabel("X")
plt.ylabel("Errors(pixels)")
plt.grid(True)
points = plt.scatter(np.array(x_eh)[:, 0],
                     np.array(x_eh)[:, 1],
                     s=1,
                     alpha=0.5)
plt.legend([points], ['Along Track Error'])

# 221表示分成2行2列，占用第二块(1行2列)
plt.subplot(222)
plt.title("Rule of residual errors across the track")
plt.xlabel("Y")
plt.ylabel("Errors(pixels)")
plt.grid(True)
points = plt.scatter(np.array(y_ev)[:, 0],
                     np.array(y_ev)[:, 1],
                     s=1,
                     alpha=0.5,
                     c='r')
plt.legend([points], ['Across Track Error'])

# 221表示分成2行2列，占用第四块(2行2列)
plt.subplot(224)
plt.title("Rule of residual errors along the track")
plt.xlabel("Y")
plt.ylabel("Errors(pixels)")
plt.grid(True)
points = plt.scatter(np.array(y_eh)[:, 0],
                     np.array(y_eh)[:, 1],
                     s=1,
                     alpha=0.5)
plt.legend([points], ['Along Track Error'])

# 最后保存绘图，dpi越高图像质量越好
plt.savefig('figure', dpi=600)
plt.show()
