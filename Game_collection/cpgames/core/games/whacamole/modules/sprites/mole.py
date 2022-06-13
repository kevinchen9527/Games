# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:Mole.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame


'''地鼠'''
class Mole(pygame.sprite.Sprite):
    def __init__(self, images, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.transform.scale(images[0], (101, 103)), 
            pygame.transform.scale(images[-1], (101, 103))
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.setPosition(position)
        self.is_hammer = False
    '''设置位置'''
    def setPosition(self, pos):
        self.rect.left, self.rect.top = pos
    '''设置被击中'''
    def setBeHammered(self):
        self.is_hammer = True
    '''显示在屏幕上'''
    def draw(self, screen):
        if self.is_hammer: self.image = self.images[1]
        screen.blit(self.image, self.rect)
    '''重置'''
    def reset(self):
        self.image = self.images[0]
        self.is_hammer = False