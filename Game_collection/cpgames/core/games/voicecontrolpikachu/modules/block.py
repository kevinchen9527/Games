# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:Block.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import cocos
import random


'''地面块'''
class Block(cocos.sprite.Sprite):
    def __init__(self, imagepath, position, **kwargs):
        super(Block, self).__init__(imagepath)
        self.image_anchor = 0, 0
        x, y = position
        if x == 0:
            self.scale_x = 4.5
            self.scale_y = 1
        else:
            self.scale_x = 0.5 + random.random() * 1.5
            self.scale_y = min(max(y - 50 + random.random() * 100, 50), 300) / 100.0
            self.position = x + 50 + random.random() * 100, 0