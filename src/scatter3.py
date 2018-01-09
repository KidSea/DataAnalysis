#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pylab as plt

from random_walk import RandomWalk



while True:

    rw = RandomWalk()
    rw.fill_walk()

    #设置绘图窗口大小的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)

    #突出起始点与重点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none')

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running  = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break