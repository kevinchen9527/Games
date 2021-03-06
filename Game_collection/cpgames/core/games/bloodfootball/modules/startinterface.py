# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:StartInterface.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame
from ....utils import QuitGame


'''定义游戏开始界面'''
def StartInterface(screen, resource_loader, cfg):
    clock = pygame.time.Clock()
    font, flag, count = resource_loader.fonts['default30'], True, 0
    font_render = font.render('按任意键开始游戏', False, cfg.RED)
    while True:
        count += 1
        if count > 20: count, flag = 0, not flag
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
            elif event.type == pygame.KEYDOWN:
                return True
        screen.blit(resource_loader.images['background_start'], (0, 0))
        if flag: screen.blit(font_render, ((cfg.SCREENSIZE[0] - font.size('按任意键开始游戏')[0]) // 2, cfg.SCREENSIZE[1] - 200))
        clock.tick(cfg.FPS)
        pygame.display.update()