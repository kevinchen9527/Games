# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:misc.py
@Time:2022/5/12 20:57

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import sys
import pygame


'''退出程序'''
def QuitGame(use_pygame=True):
    if use_pygame: pygame.quit()
    sys.exit()