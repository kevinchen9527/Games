# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:Hammer.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame


'''锤子类'''
class Hammer(pygame.sprite.Sprite):
    def __init__(self, images, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.images[1])
        self.rect.left, self.rect.top = position
        # 用于显示锤击时的特效
        self.hammer_count = 0
        self.hammer_last_time = 4
        self.is_hammering = False
    '''设置位置'''
    def setPosition(self, pos):
        self.rect.centerx, self.rect.centery = pos
    '''设置hammering'''
    def setHammering(self):
        self.is_hammering = True
    '''显示在屏幕上'''
    def draw(self, screen):
        if self.is_hammering:
            self.image = self.images[1]
            self.hammer_count += 1
            if self.hammer_count > self.hammer_last_time:
                self.is_hammering = False
                self.hammer_count = 0
        else:
            self.image = self.images[0]
        screen.blit(self.image, self.rect)