# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:Hero.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame


'''定义hero'''
class Hero(pygame.sprite.Sprite):
    def __init__(self, image, coordinate, block_size, border_size, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (block_size, block_size))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = coordinate[0] * block_size + border_size[0], coordinate[1] * block_size + border_size[1]
        self.coordinate = coordinate
        self.block_size = block_size
        self.border_size = border_size
    '''移动'''
    def move(self, direction, maze):
        blocks_list = maze.blocks_list
        if direction == 'up':
            if blocks_list[self.coordinate[1]][self.coordinate[0]].has_walls[0]:
                return False
            else:
                self.coordinate[1] = self.coordinate[1] - 1
                return True
        elif direction == 'down':
            if blocks_list[self.coordinate[1]][self.coordinate[0]].has_walls[1]:
                return False
            else:
                self.coordinate[1] = self.coordinate[1] + 1
                return True
        elif direction == 'left':
            if blocks_list[self.coordinate[1]][self.coordinate[0]].has_walls[2]:
                return False
            else:
                self.coordinate[0] = self.coordinate[0] - 1
                return True
        elif direction == 'right':
            if blocks_list[self.coordinate[1]][self.coordinate[0]].has_walls[3]:
                return False
            else:
                self.coordinate[0] = self.coordinate[0] + 1
                return True
        else:
            raise ValueError('Unsupport direction %s in Hero.move...' % direction)
    '''绑定到屏幕'''
    def draw(self, screen):
        self.rect.left, self.rect.top = self.coordinate[0] * self.block_size + self.border_size[0], self.coordinate[1] * self.block_size + self.border_size[1]
        screen.blit(self.image, self.rect)