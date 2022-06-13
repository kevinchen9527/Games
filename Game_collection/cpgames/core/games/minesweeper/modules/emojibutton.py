# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:EmojiButton.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame


'''表情按钮'''
class EmojiButton(pygame.sprite.Sprite):
    def __init__(self, images, position, status_code=0, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        # 导入图片
        self.images = images
        self.image = self.images['face_normal']
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        # 表情按钮的当前状态
        self.status_code = status_code
    '''画到屏幕上'''
    def draw(self, screen):
        # 状态码为0, 代表正常的表情
        if self.status_code == 0:
            self.image = self.images['face_normal']
        # 状态码为1, 代表失败的表情
        elif self.status_code == 1:
            self.image = self.images['face_fail']
        # 状态码为2, 代表成功的表情
        elif self.status_code == 2:
            self.image = self.images['face_success']
        # 绑定图片到屏幕
        screen.blit(self.image, self.rect)
    '''设置当前的按钮的状态'''
    def setstatus(self, status_code):
        self.status_code = status_code