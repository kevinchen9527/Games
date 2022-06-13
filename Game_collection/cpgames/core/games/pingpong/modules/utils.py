# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:loadImage.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame


'''导入图片'''
def loadImage(imgpath, transparent=True):
    img = pygame.image.load(imgpath)
    img = img.convert()
    if transparent:
        color = img.get_at((0, 0))
        img.set_colorkey(color, pygame.RLEACCEL)
    return img