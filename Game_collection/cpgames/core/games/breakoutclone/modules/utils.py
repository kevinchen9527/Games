# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:utils.py
@Time:2022/5/25 17:01

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""


'''导入关卡文件'''
def loadLevel(levelpath):
    brick_positions = []
    fp = open(levelpath, 'r', encoding='utf-8')
    y = -1
    for line in fp.readlines():
        if (not line.strip()) or (line.startswith('#')):
            continue
        else:
            y += 1
            x = -1
            for c in line:
                x += 1
                if c == 'B':
                    brick_positions.append([x, y])
    return brick_positions