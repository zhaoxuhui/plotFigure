# coding=utf-8
from matplotlib import pyplot as plt
import numpy as np
import sys
import pickle


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


if __name__ == '__main__':
    if sys.argv.__len__() == 2 and sys.argv[1] == 'help':
        print(">>>Python script for plotting error figure<<<")
        print("\nUsage instruction:")
        print("python plotFigure.py [data_path] [figure_outpath] [grid_width] [grid_height]")
        print("\n[data_path]:The path of input text data file.")
        print("[figure_outpath]:The output path of figure.")
        print("[grid_width]:The width of figure.Note that this is not the real width of output figure."
              "It only represents the ratio relationship between real width and height.")
        print("[grid_height]:The height of figure.Note that this is not the real height of output figure."
              "It only represents the ratio relationship between real width and height.")
        print("\nUsage example:")
        print("python plotFigure.py "
              "C:\Desktop\SC_Accuracy_Ru.txt "
              "C:\Desktop\out.png 16 10")
    elif sys.argv.__len__() == 5:
        print("Reading data...")
        x_ev, x_eh, y_ev, y_eh = readData(sys.argv[1])
        print("Read data success.")

        test = open("test.txt", 'w')
        pickle.dump(x_ev, test)
        test.close()

        print("\nPlotting figure...")
        grid_w = int(sys.argv[3])
        grid_h = int(sys.argv[4])
        plt.figure(figsize=(grid_w, grid_h))
        print("Figure grid width:" + grid_w.__str__())
        print("Figure grid height:" + grid_h.__str__())

        plt.subplot(221)
        plt.title("Rule of residual errors across the track")
        plt.xlabel("X")
        plt.ylabel("Errors(pixels)")
        # 用于设置y轴范围
        plt.ylim((-10, 10))
        # 用于设置y轴坐标间隔
        plt.yticks(np.arange(-10, 10, 5))
        plt.grid(True)
        points = plt.scatter(np.array(x_ev)[:, 0],
                             np.array(x_ev)[:, 1],
                             s=1,
                             alpha=0.5,
                             c='r')
        # loc属性用于设置图例位置
        plt.legend([points], ['Across Track Error'], loc='upper right')

        plt.subplot(223)
        plt.title("Rule of residual errors along the track")
        plt.xlabel("X")
        plt.ylabel("Errors(pixels)")
        plt.ylim((-10, 10))
        plt.yticks(np.arange(-10, 10, 5))
        plt.grid(True)
        points = plt.scatter(np.array(x_eh)[:, 0],
                             np.array(x_eh)[:, 1],
                             s=1,
                             alpha=0.5)
        plt.legend([points], ['Along Track Error'], loc='upper right')

        plt.subplot(222)
        plt.title("Rule of residual errors across the track")
        plt.xlabel("Y")
        plt.ylabel("Errors(pixels)")
        plt.ylim((-10, 10))
        plt.yticks(np.arange(-10, 10, 5))
        plt.grid(True)
        points = plt.scatter(np.array(y_ev)[:, 0],
                             np.array(y_ev)[:, 1],
                             s=1,
                             alpha=0.5,
                             c='r')
        plt.legend([points], ['Across Track Error'], loc='upper right')

        plt.subplot(224)
        plt.title("Rule of residual errors along the track")
        plt.xlabel("Y")
        plt.ylabel("Errors(pixels)")
        plt.ylim((-10, 10))
        plt.yticks(np.arange(-10, 10, 5))
        plt.grid(True)
        points = plt.scatter(np.array(y_eh)[:, 0],
                             np.array(y_eh)[:, 1],
                             s=1,
                             alpha=0.5)
        plt.legend([points], ['Along Track Error'], loc='upper right')

        print("Plot figure success.")

        print("\nSaving figure...")
        plt.savefig(sys.argv[2], dpi=600)
        print("Save figure success.")
        plt.show()

    else:
        print("Input 'python plotFigure.py help' to get help information.")
