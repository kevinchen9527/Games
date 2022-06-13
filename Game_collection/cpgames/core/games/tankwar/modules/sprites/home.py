# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:Home.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame


'''大本营类'''
class Home(pygame.sprite.Sprite):
    def __init__(self, position, images, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.alive = True
    '''被摧毁'''
    def setDead(self):
        self.image = self.images[1]
        self.alive = False
    '''画到屏幕上'''
    def draw(self, screen):
        screen.blit(self.image, self.rect)