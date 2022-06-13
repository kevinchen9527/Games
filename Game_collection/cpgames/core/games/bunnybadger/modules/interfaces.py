# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:interfaces.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame
from ....utils import QuitGame


'''游戏结束界面'''
def ShowEndGameInterface(screen, exitcode, accuracy, game_images, font):
    text = font.render(f"Accuracy: {accuracy}%", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 24
    while True:
        screen.fill(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
        if exitcode:
            screen.blit(game_images['youwin'], (0, 0))
        else:
            screen.blit(game_images['gameover'], (0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()