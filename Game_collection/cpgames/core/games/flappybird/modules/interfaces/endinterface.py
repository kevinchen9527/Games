# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:endinterface.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import pygame
from .....utils import QuitGame


'''游戏结束界面'''
def GameEndIterface(screen, sounds, showScore, score, number_images, bird, pipe_sprites, backgroud_image, other_images, base_pos, cfg):
    sounds['die'].play()
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                QuitGame()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    return
        boundary_values = [0, base_pos[-1]]
        bird.update(boundary_values, float(clock.tick(cfg.FPS))/1000.)
        screen.blit(backgroud_image, (0, 0))
        pipe_sprites.draw(screen)
        screen.blit(other_images['base'], base_pos)
        showScore(cfg, screen, score, number_images)
        bird.draw(screen)
        pygame.display.update()
        clock.tick(cfg.FPS)