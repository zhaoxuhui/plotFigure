# coding=utf-8
from matplotlib import pyplot as plt
import numpy as np


def readData(file_path):
    text_file = open(file_path)
    data_item = []
    x_ev = []
    x_eh = []
    y_ev = []
    y_eh = []

    line = text_file.readline().strip('\n')
    while line:
        line = text_file.readline().strip('\n')
        if line != '':
            data_item.append(line)

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

    x_ev.sort()
    x_eh.sort()
    y_eh.sort()
    y_ev.sort()
    return x_ev, x_eh, y_ev, y_eh


def plotFigure(file_path, img_outpath, grid_w=16, grid_h=10, y_range_min=-10, y_range_max=10, y_step=5):
    """

    :param file_path: 输入数据文件路径
    :param img_outpath: 输出影像文件路径
    :param grid_w: 影像格网宽度，默认16
    :param grid_h: 影像格网高度，默认10
    :param y_range_min: y轴最小值，默认-10
    :param y_range_max: y轴最大值，默认10
    :param y_step: y轴步长，默认5
    :return: 空
    """

    print("Reading data...")
    x_ev, x_eh, y_ev, y_eh = readData(file_path)
    print("Read data success.")

    print("\nPlotting figure...")
    plt.figure(figsize=(grid_w, grid_h))
    print("Figure grid width:" + grid_w.__str__())
    print("Figure grid height:" + grid_h.__str__())

    plt.subplot(221)
    plt.title("Rule of residual errors across the track")
    plt.xlabel("X")
    plt.ylabel("Errors(pixels)")
    plt.ylim((y_range_min, y_range_max))
    plt.yticks(np.arange(y_range_min, y_range_max, y_step))
    plt.grid(True)
    points = plt.scatter(np.array(x_ev)[:, 0],
                         np.array(x_ev)[:, 1],
                         s=1,
                         alpha=0.5,
                         c='r')
    plt.legend([points], ['Across Track Error'], loc='upper right')

    plt.subplot(223)
    plt.title("Rule of residual errors along the track")
    plt.xlabel("X")
    plt.ylabel("Errors(pixels)")
    plt.ylim((y_range_min, y_range_max))
    plt.yticks(np.arange(y_range_min, y_range_max, y_step))
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
    plt.ylim((y_range_min, y_range_max))
    plt.yticks(np.arange(y_range_min, y_range_max, y_step))
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
    plt.ylim((y_range_min, y_range_max))
    plt.yticks(np.arange(y_range_min, y_range_max, y_step))
    plt.grid(True)
    points = plt.scatter(np.array(y_eh)[:, 0],
                         np.array(y_eh)[:, 1],
                         s=1,
                         alpha=0.5)
    plt.legend([points], ['Along Track Error'], loc='upper right')

    print("Plot figure success.")

    print("\nSaving figure...")
    plt.savefig(img_outpath, dpi=600)
    print("Save figure success.")
    plt.show()
