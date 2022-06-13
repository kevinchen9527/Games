# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:Config.py
@Time:2022/5/12 20:57

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import os
import random
import pygame
from ...utils import QuitGame
from ..base import PygameBaseGame
from .modules import aircraftSprite, ufoSprite, enemySprite, myBulletSprite, enemyBulletSprite, showLife, showText, endInterface


'''配置类'''
class Config():
    # 根目录
    rootdir = os.path.split(os.path.abspath(__file__))[0]
    # 一些颜色
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (50, 250, 5)
    RED = (255, 0, 0)
    # FPS
    FPS = 60
    # 背景音乐路径
    BGM_PATH = os.path.join(rootdir, 'resources/bgm.mp3')
    # 最高分保存路径
    HIGHEST_SCORE_SAVE_PATH = os.path.join(rootdir, 'score')
    # 屏幕大小
    SCREENSIZE = (800, 600)
    # 标题
    TITLE = '外星人入侵小游戏'
    # 字体路径
    FONT_PATHS_DICT = {
        'default18': {'name': 'arial', 'size': 18, 'system_font': True},
        'default30': {'name': 'arial', 'size': 30, 'system_font': True},
    }


'''外星人入侵小游戏'''
class AlienInvasionGame(PygameBaseGame):
    game_type = 'alieninvasion'
    def __init__(self, **kwargs):
        self.cfg = Config
        super(AlienInvasionGame, self).__init__(config=self.cfg, **kwargs)
    '''运行游戏'''
    def run(self):
        # 初始化
        screen, resource_loader, cfg = self.screen, self.resource_loader, self.cfg
        # 播放背景音乐
        resource_loader.playbgm()
        # 游戏主循环
        while True:
            is_win = self.GamingInterface(screen, cfg, resource_loader)
            endInterface(screen, cfg.BLACK, is_win, cfg, resource_loader)
    '''开始游戏'''
    def GamingInterface(self, screen, cfg, resource_loader):
        clock = pygame.time.Clock()
        # 加载字体
        font = resource_loader.fonts['default18']
        if not os.path.isfile('score'):
            f = open(cfg.HIGHEST_SCORE_SAVE_PATH, 'w')
            f.write('0')
            f.close()
        with open(cfg.HIGHEST_SCORE_SAVE_PATH, 'r') as f:
            highest_score = int(f.read().strip())
        # 敌方
        enemies_group = pygame.sprite.Group()
        for i in range(55):
            if i < 11:
                enemy = enemySprite('small', i, cfg.WHITE, cfg.WHITE)
            elif i < 33:
                enemy = enemySprite('medium', i, cfg.WHITE, cfg.WHITE)
            else:
                enemy = enemySprite('large', i, cfg.WHITE, cfg.WHITE)
            enemy.rect.x = 85 + (i % 11) * 50
            enemy.rect.y = 120 + (i // 11) * 45
            enemies_group.add(enemy)
        boomed_enemies_group = pygame.sprite.Group()
        en_bullets_group = pygame.sprite.Group()
        ufo = ufoSprite(color=cfg.RED)
        # 我方
        myaircraft = aircraftSprite(color=cfg.GREEN, bullet_color=cfg.WHITE)
        my_bullets_group = pygame.sprite.Group()
        # 用于控制敌方位置更新
        # --移动一行
        enemy_move_count = 24
        enemy_move_interval = 24
        enemy_move_flag = False
        # --改变移动方向(改变方向的同时集体下降一次)
        enemy_change_direction_count = 0
        enemy_change_direction_interval = 60
        enemy_need_down = False
        enemy_move_right = True
        enemy_need_move_row = 6
        enemy_max_row = 5
        # 用于控制敌方发射子弹
        enemy_shot_interval = 100
        enemy_shot_count = 0
        enemy_shot_flag = False
        # 游戏进行中
        running = True
        is_win = False
        # 主循环
        while running:
            screen.fill(cfg.BLACK)
            for event in pygame.event.get():
                # --点右上角的X或者按Esc键退出游戏
                if event.type == pygame.QUIT:
                    QuitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        QuitGame()
                # --射击
                if event.type == pygame.MOUSEBUTTONDOWN:
                    my_bullet = myaircraft.shot()
                    if my_bullet:
                        my_bullets_group.add(my_bullet)
            # --我方子弹与敌方/UFO碰撞检测
            for enemy in enemies_group:
                if pygame.sprite.spritecollide(enemy, my_bullets_group, True, None):
                    boomed_enemies_group.add(enemy)
                    enemies_group.remove(enemy)
                    myaircraft.score += enemy.reward
            if pygame.sprite.spritecollide(ufo, my_bullets_group, True, None):
                ufo.is_dead = True
                myaircraft.score += ufo.reward
            # --更新并画敌方
            # ----敌方子弹
            enemy_shot_count += 1
            if enemy_shot_count > enemy_shot_interval:
                enemy_shot_flag = True
                enemies_survive_list = [enemy.number for enemy in enemies_group]
                shot_number = random.choice(enemies_survive_list)
                enemy_shot_count = 0
            # ----敌方移动
            enemy_move_count += 1
            if enemy_move_count > enemy_move_interval:
                enemy_move_count = 0
                enemy_move_flag = True
                enemy_need_move_row -= 1
                if enemy_need_move_row == 0:
                    enemy_need_move_row = enemy_max_row
                enemy_change_direction_count += 1
                if enemy_change_direction_count > enemy_change_direction_interval:
                    enemy_change_direction_count = 1
                    enemy_move_right = not enemy_move_right
                    enemy_need_down = True
                    # ----每次下降提高移动和射击速度
                    enemy_move_interval = max(15, enemy_move_interval-3)
                    enemy_shot_interval = max(50, enemy_move_interval-10)
            # ----遍历更新
            for enemy in enemies_group:
                if enemy_shot_flag:
                    if enemy.number == shot_number:
                        en_bullet = enemy.shot()
                        en_bullets_group.add(en_bullet)
                if enemy_move_flag:
                    if enemy.number in range((enemy_need_move_row-1)*11, enemy_need_move_row*11):
                        if enemy_move_right:
                            enemy.update('right', cfg.SCREENSIZE[1])
                        else:
                            enemy.update('left', cfg.SCREENSIZE[1])
                else:
                    enemy.update(None, cfg.SCREENSIZE[1])
                if enemy_need_down:
                    if enemy.update('down', cfg.SCREENSIZE[1]):
                        running = False
                        is_win = False
                    enemy.change_count -= 1
                enemy.draw(screen)
            enemy_move_flag = False
            enemy_need_down = False
            enemy_shot_flag = False
            # ----敌方爆炸特效
            for boomed_enemy in boomed_enemies_group:
                if boomed_enemy.boom(screen):
                    boomed_enemies_group.remove(boomed_enemy)
                    del boomed_enemy
            # --敌方子弹与我方飞船碰撞检测
            if not myaircraft.one_dead:
                if pygame.sprite.spritecollide(myaircraft, en_bullets_group, True, None):
                    myaircraft.one_dead = True
            if myaircraft.one_dead:
                if myaircraft.boom(screen):
                    myaircraft.resetBoom()
                    myaircraft.num_life -= 1
                    if myaircraft.num_life < 1:
                        running = False
                        is_win = False
            else:
                # ----更新飞船
                myaircraft.update(cfg.SCREENSIZE[0])
                # ----画飞船
                myaircraft.draw(screen)
            if (not ufo.has_boomed) and (ufo.is_dead):
                if ufo.boom(screen):
                    ufo.has_boomed = True
            else:
                # ----更新UFO
                ufo.update(cfg.SCREENSIZE[0])
                # ----画UFO
                ufo.draw(screen)
            # --画我方飞船子弹
            for bullet in my_bullets_group:
                if bullet.update():
                    my_bullets_group.remove(bullet)
                    del bullet
                else:
                    bullet.draw(screen)
            # --画敌方子弹
            for bullet in en_bullets_group:
                if bullet.update(cfg.SCREENSIZE[1]):
                    en_bullets_group.remove(bullet)
                    del bullet
                else:
                    bullet.draw(screen)
            if myaircraft.score > highest_score:
                highest_score = myaircraft.score
            # --得分每增加2000我方飞船增加一条生命
            if (myaircraft.score % 2000 == 0) and (myaircraft.score > 0) and (myaircraft.score != myaircraft.old_score):
                myaircraft.old_score = myaircraft.score
                myaircraft.num_life = min(myaircraft.num_life + 1, myaircraft.max_num_life)
            # --敌人都死光了的话就胜利了
            if len(enemies_group) < 1:
                is_win = True
                running = False
            # --显示文字
            # ----当前得分
            showText(screen, 'SCORE: ', cfg.WHITE, font, 200, 8)
            showText(screen, str(myaircraft.score), cfg.WHITE, font, 200, 24)
            # ----敌人数量
            showText(screen, 'ENEMY: ', cfg.WHITE, font, 370, 8)
            showText(screen, str(len(enemies_group)), cfg.WHITE, font, 370, 24)
            # ----历史最高分
            showText(screen, 'HIGHEST: ', cfg.WHITE, font, 540, 8)
            showText(screen, str(highest_score), cfg.WHITE, font, 540, 24)
            # ----FPS
            showText(screen, 'FPS: ' + str(int(clock.get_fps())), cfg.RED, font, 8, 8)
            # --显示剩余生命值
            showLife(screen, myaircraft.num_life, cfg.GREEN)
            pygame.display.update()
            clock.tick(cfg.FPS)
        with open(cfg.HIGHEST_SCORE_SAVE_PATH, 'w') as f:
            f.write(str(highest_score))
        return is_win