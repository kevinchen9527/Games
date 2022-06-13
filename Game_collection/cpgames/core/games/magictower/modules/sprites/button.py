# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:Button.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame


'''按钮类'''
class Button(pygame.sprite.Sprite):
    def __init__(self, text, fontpath, fontsize, position, color_selected=(255, 0, 0), color_default=(255, 255, 255)):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.color_selected = color_selected
        self.color_default = color_default
        self.font = pygame.font.Font(fontpath, fontsize)
        self.font_render = self.font.render(text, True, color_default)
        self.rect = self.font_render.get_rect()
        self.rect.center = position
    '''更新函数: 不断地更新检测鼠标是否在按钮上'''
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.font_render = self.font.render(self.text, True, self.color_selected)
        else:
            self.font_render = self.font.render(self.text, True, self.color_default)
    '''绑定到屏幕上'''
    def draw(self, screen):
        screen.blit(self.font_render, self.rect)