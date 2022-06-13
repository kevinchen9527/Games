# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:utils.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame


'''画游戏网格'''
def drawGameGrid(cfg, screen):
    color = (40, 40, 40)
    for x in range(0, cfg.SCREENSIZE[0], cfg.BLOCK_SIZE):
        pygame.draw.line(screen, color, (x, 0), (x, cfg.SCREENSIZE[1]))
    for y in range(0, cfg.SCREENSIZE[1], cfg.BLOCK_SIZE):
        pygame.draw.line(screen, color, (0, y), (cfg.SCREENSIZE[0], y))


'''显示得分'''
def showScore(cfg, score, screen, resource_loader):
    color = (255, 255, 255)
    font = resource_loader.fonts['default30']
    text = font.render('Score: %s' % score, True, color)
    rect = text.get_rect()
    rect.topleft = (10, 10)
    screen.blit(text, rect)