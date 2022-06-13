# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:Pikachu.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import cocos


'''皮卡丘类'''
class Pikachu(cocos.sprite.Sprite):
    def __init__(self, imagepath, **kwargs):
        super(Pikachu, self).__init__(imagepath)
        # 锚点
        self.image_anchor = 0, 0
        # 初始重置
        self.reset(False)
        # 更新
        self.schedule(self.update)
    '''声控跳跃'''
    def jump(self, h):
        if self.is_able_jump:
            self.y += 1
            self.speed -= max(min(h, 10), 7)
            self.is_able_jump = False
    '''着陆后静止'''
    def land(self, y):
        if self.y > y - 25:
            self.is_able_jump = True
            self.speed = 0
            self.y = y
    '''更新(重力下降)'''
    def update(self, dt):
        self.speed += 10 * dt
        self.y -= self.speed
        if self.y < -85:
            self.reset()
    '''重置'''
    def reset(self, flag=True):
        if flag: self.parent.reset()
        # 是否可跳跃
        self.is_able_jump = False
        # 速度
        self.speed = 0
        # 位置
        self.position = 80, 280