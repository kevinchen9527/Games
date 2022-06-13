# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:Chessman.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
from .utils import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


'''棋子类'''
class Chessman(QLabel):
    def __init__(self, imagepath, parent=None, **kwargs):
        super(Chessman, self).__init__(parent)
        self.color = imagepath.split('.')[-2][-5:]
        self.image = QPixmap(imagepath)
        self.setFixedSize(self.image.size())
        self.setPixmap(self.image)
    def move(self, point):
        x, y = Pixel2Chesspos(point)
        x = 30 * x + 50 - self.image.width() / 2
        y = 30 * y + 50 - self.image.height() / 2
        super().move(x, y)