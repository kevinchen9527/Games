# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:pusherSprite.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame


'''推箱子的人精灵类'''
class pusherSprite(pygame.sprite.Sprite):
    def __init__(self, col, row, cfg, resource_loader):
        pygame.sprite.Sprite.__init__(self)
        self.image = resource_loader.images['player'].convert()
        color = self.image.get_at((0, 0))
        self.image.set_colorkey(color, pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.col = col
        self.row = row
    '''移动'''
    def move(self, direction, is_test=False):
        # 测试模式代表模拟移动
        if is_test:
            if direction == 'up':
                return self.col, self.row - 1
            elif direction == 'down':
                return self.col, self.row + 1
            elif direction == 'left':
                return self.col - 1, self.row
            elif direction == 'right':
                return self.col + 1, self.row
        else:
            if direction == 'up':
                self.row -= 1
            elif direction == 'down':
                self.row += 1
            elif direction == 'left':
                self.col -= 1
            elif direction == 'right':
                self.col += 1
    '''将人物画到游戏界面上'''
    def draw(self, screen):
        self.rect.x = self.rect.width * self.col
        self.rect.y = self.rect.height * self.row
        screen.blit(self.image, self.rect)


'''游戏元素精灵类'''
class elementSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, col, row, cfg, resource_loader):
        pygame.sprite.Sprite.__init__(self)
        # 导入box.png/target.png/wall.png
        self.image = resource_loader.images[sprite_name].convert()
        color = self.image.get_at((0, 0))
        self.image.set_colorkey(color, pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        # 元素精灵类型
        self.sprite_type = sprite_name.split('.')[0]
        # 元素精灵的位置
        self.col = col
        self.row = row
    '''将游戏元素画到游戏界面上'''
    def draw(self, screen):
        self.rect.x = self.rect.width * self.col
        self.rect.y = self.rect.height * self.row
        screen.blit(self.image, self.rect)
    '''移动游戏元素'''
    def move(self, direction, is_test=False):
        if self.sprite_type == 'box':
            # 测试模式代表模拟移动
            if is_test:
                if direction == 'up':
                    return self.col, self.row - 1
                elif direction == 'down':
                    return self.col, self.row + 1
                elif direction == 'left':
                    return self.col - 1, self.row
                elif direction == 'right':
                    return self.col + 1, self.row
            else:
                if direction == 'up':
                    self.row -= 1
                elif direction == 'down':
                    self.row += 1
                elif direction == 'left':
                    self.col -= 1
                elif direction == 'right':
                    self.col += 1