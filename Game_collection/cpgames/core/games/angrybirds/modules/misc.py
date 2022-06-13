# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:VelocityVector.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import math


'''定义速度向量'''
class VelocityVector():
    def __init__(self, magnitude=0, angle=math.radians(0)):
        self.angle = angle
        self.magnitude = magnitude


'''向量相加'''
def VectorAddition(vector1, vector2):
    x = math.sin(vector1.angle) * vector1.magnitude + math.sin(vector2.angle) * vector2.magnitude
    y = math.cos(vector1.angle) * vector1.magnitude + math.cos(vector2.angle) * vector2.magnitude
    angle = 0.5 * math.pi - math.atan2(y, x)
    magnitude = math.hypot(x, y)
    return VelocityVector(magnitude, angle)