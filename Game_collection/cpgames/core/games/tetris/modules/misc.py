# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:misc.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
from PyQt5.QtGui import *


'''给板块的一个Cell填色'''
def drawCell(painter, x, y, shape, grid_size):
    colors = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC, 0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
    if shape == 0:
        return
    color = QColor(colors[shape])
    painter.fillRect(x + 1, y + 1, grid_size - 2, grid_size - 2, color)
    painter.setPen(color.lighter())
    painter.drawLine(x, y + grid_size - 1, x, y)
    painter.drawLine(x, y, x + grid_size - 1, y)
    painter.setPen(color.darker())
    painter.drawLine(x + 1, y + grid_size - 1, x + grid_size - 1, y + grid_size - 1)
    painter.drawLine(x + grid_size - 1, y + grid_size - 1, x + grid_size - 1, y + 1)