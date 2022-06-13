# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:Apple.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import random
import pygame


'''食物类'''
class Apple(pygame.sprite.Sprite):
    def __init__(self, cfg, snake_coords, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.cfg = cfg
        while True:
            self.coord = [random.randint(0, cfg.GAME_MATRIX_SIZE[0]-1), random.randint(0, cfg.GAME_MATRIX_SIZE[1]-1)]
            if self.coord not in snake_coords:
                break
        self.color = (255, 0, 0)
    '''画到屏幕上'''
    def draw(self, screen):
        cx, cy = int((self.coord[0] + 0.5) * self.cfg.BLOCK_SIZE), int((self.coord[1] + 0.5) * self.cfg.BLOCK_SIZE)
        pygame.draw.circle(screen, self.color, (cx, cy), self.cfg.BLOCK_SIZE//2-2)