# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:TextBoard.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame


'''文字板'''
class TextBoard(pygame.sprite.Sprite):
    def __init__(self, text, font, position, color, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.font = font
        self.position = position
        self.color = color
    def draw(self, screen):
        text_render = self.font.render(self.text, True, self.color)
        screen.blit(text_render, self.position)
    def update(self, text):
        self.text = text