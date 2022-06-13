# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址):
@File:cpgames.py
@Time:2022/5/12 20:57

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import sys
import warnings
from PyQt5.QtWidgets import QApplication
import tkinter as tk

if __name__ == '__main__':
    from core import *
else:
    from .core import *
warnings.filterwarnings('ignore')

'''Python实用工具集'''


class CPGames():
    def __init__(self, **kwargs):
        for key, value in kwargs.items(): 
            setattr(self, key, value)
        self.supported_games = self.initialize()

    '''执行对应的小程序'''

    def execute(self, game_type=None, config={}):
        assert game_type in self.supported_games, 'unsupport game_type %s...' % game_type
        qt_games = ['tetris', 'gobang']
        if game_type in qt_games:
            app = QApplication(sys.argv)
            client = self.supported_games[game_type](**config)
            client.show()
            sys.exit(app.exec_())
        else:
            client = self.supported_games[game_type](**config)
            client.run()

    '''初始化'''

    def initialize(self):
        supported_games = {
            'ski': SkiGame,
            'maze': MazeGame,
            'gobang': GobangGame,
            'tetris': TetrisGame,
            'pacman': PacmanGame,
            'gemgem': GemGemGame,
            'tankwar': TankWarGame,
            'sokoban': SokobanGame,
            'pingpong': PingpongGame,
            'trexrush': TRexRushGame,
            'bomberman': BomberManGame,
            'whacamole': WhacAMoleGame,
            'catchcoins': CatchCoinsGame,
            'flappybird': FlappyBirdGame,
            'angrybirds': AngryBirdsGame,
            'magictower': MagicTowerGame,
            'aircraftwar': AircraftWarGame,
            'bunnybadger': BunnyBadgerGame,
            'minesweeper': MineSweeperGame,
            'greedysnake': GreedySnakeGame,
            'puzzlepieces': PuzzlePiecesGame,
            'towerdefense': TowerDefenseGame,
            'bloodfootball': BloodFootballGame,
            'alieninvasion': AlienInvasionGame,
            'breakoutclone': BreakoutcloneGame,
            'twentyfourpoint': TwentyfourPointGame,
            'flipcardbymemory': FlipCardByMemoryGame,
            'twozerofoureight': TwoZeroFourEightGame,
            'voicecontrolpikachu': VoiceControlPikachuGame,
        }
        return supported_games

    '''获得所有支持的游戏信息'''

    def getallsupported(self):
        all_supports = {}
        for key, value in self.supported_games.items():
            all_supports[value.game_type] = key
        return all_supports


def printf_button(f):
    print('用户点击了啥', type(f))
    games_client.execute(f)


def createButton(supported_games_name):
    root = tk.Tk()
    root.title('游戏选择窗口')
    root.geometry('600x300+100+100')
    ButtonList = []
    for _ in range(len(supported_games_name)):
        ButtonList.append(0)  # 创建储存按钮对象的列表
    sx = 20
    ssx = 20
    sssx = 20
    ssssx = 20
    i = 0
    for k, v in supported_games_name.items():
        i += 1
        if sx <= 540:
            ButtonList[i - 1] = tk.Button(root, text=v, bg="white", width=7, height=2, justify='center', fg='black',
                                          command=lambda f=k: printf_button(f))
            ButtonList[i - 1].place(x=sx, y=20)
        else:
            if ssx <= 540:
                ButtonList[i - 1] = tk.Button(root, text=v, bg="white", width=7, height=2, justify='center', fg='black',
                                              command=lambda f=k: printf_button(f))
                ButtonList[i - 1].place(x=ssx, y=80)
            else:
                if sssx <= 540:
                    ButtonList[i - 1] = tk.Button(root, text=v, bg="white", width=7, height=2, justify='center',
                                                  fg='black', command=lambda f=k: printf_button(f))
                    ButtonList[i - 1].place(x=sssx, y=140)
                else:
                    ButtonList[i - 1] = tk.Button(root, text=v, bg="white", width=7, height=2, justify='center',
                                                  fg='black', command=lambda f=k: printf_button(f))
                    ButtonList[i - 1].place(x=ssssx, y=200)
                    ssssx += 60
                sssx += 60
            ssx += 60
        sx += 60
    root.mainloop()


def init_game_name():
    supported_games_name = {
        'ski': '滑雪',
        'maze': '走迷宫',
        'gobang': '五子棋',
        'tetris': '俄罗斯方块',
        'pacman': '吃豆人',
        'gemgem': '消消乐',
        'tankwar': '坦克大战',
        'sokoban': '推箱子',
        'pingpong': '乒乓球',
        'trexrush': '恐龙快跑',
        'bomberman': '炸弹人',
        'whacamole': '打地鼠',
        'catchcoins': '接金币',
        'flappybird': '飞翔的小鸟',
        'angrybirds': '愤怒的小鸟',
        'magictower': '魔塔',
        'aircraftwar': '飞机大战',
        'bunnybadger': '兔子和獾',
        'minesweeper': '扫雷',
        'greedysnake': '贪吃蛇',
        'puzzlepieces': '拼图',
        'towerdefense': '塔防',
        'bloodfootball': '热血足球',
        'alieninvasion': '外星人入侵',
        'breakoutclone': '打砖块',
        'twentyfourpoint': '24点',
        'flipcardbymemory': '记忆翻牌',
        'twozerofoureight': '2048',
        'voicecontrolpikachu': '八分音符',
    }
    return supported_games_name




if __name__ == '__main__':
    supported_games_name = init_game_name()
    games_client = CPGames()
    # all_supports = games_client.getallsupported()
    createButton(supported_games_name)
