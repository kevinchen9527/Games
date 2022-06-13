# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:安然
@Blog(个人博客地址): 
@File:fruit_machine.py
@Time:2022/5/13 16:27

@Motto:不积跬步无以至千里，不积小流无以成江海，程序人生的精彩需要坚持不懈地积累！
"""
import random
import tkinter


class tiger_machine:
    def __init__(self):
        self.windows = None
        self.recoder_index = -1
        self.chinese_dict = {0: ['橘子', None], 1: ['大铃铛', None], 2: ['小鬼', None], 3: ['大鬼', None], 4: ['中鬼', None],
                             5: ['苹果', None], 6: ['大芒果', None],
                             7: ['小铃铛', None], 8: ['苹果', None], 9: ['火车', None], 10: ['小双星', None], 11: ['大双星', None],
                             12: ['大芒果', None], 13: ['小芒果', None],
                             14: ['大7', None], 15: ['空', None], 16: ['小7', None], 17: ['大铃铛', None], 18: ['大橘子', None],
                             19: ['大西瓜', None], 20: ['小西瓜', None], 21: ['打枪', None], 22: ['苹果', None],
                             23: ['小橘子', None]}

        self.recoder_list = {}  # 统计奖励出现的次数

    def create_windows(self):
        """
        创建面板
        :return:
        """
        self.windows = tkinter.Tk()
        self.windows.title('水果机')
        self.windows.minsize(400, 400)
        self.auto_product_button()

        def run():
            self.lottery_draw()

        btm13 = tkinter.Button(self.windows, text="开始", bg="pink", command=run)
        btm13.place(x=90, y=125, width=50, height=50)

        self.windows.mainloop()

    def auto_product_button(self):
        """
        自动生成面板上的按钮（每7个 是一列 或者一排）
        :return:
        """
        x = 20
        for i in range(7):
            self.chinese_dict[i][1] = tkinter.Button(self.windows, text=self.chinese_dict[i][0], bg="pink")
            self.chinese_dict[i][1].place(x=x, y=20, width=50, height=50)
            x += 50

        y = 70
        for i in range(7, 13):
            self.chinese_dict[i][1] = tkinter.Button(self.windows, text=self.chinese_dict[i][0], bg="pink")
            self.chinese_dict[i][1].place(x=20, y=y, width=50, height=50)
            y += 50

        x = 70
        for i in range(13, 19):
            self.chinese_dict[i][1] = tkinter.Button(self.windows, text=self.chinese_dict[i][0], bg="pink")
            self.chinese_dict[i][1].place(x=x, y=320, width=50, height=50)
            x += 50

        y = 70
        for i in range(19, 24):
            self.chinese_dict[i][1] = tkinter.Button(self.windows, text=self.chinese_dict[i][0], bg="pink")
            self.chinese_dict[i][1].place(x=320, y=y, width=50, height=50)
            y += 50

    def lottery_draw(self):
        """
        开始抽奖
        :return:
        """
        if self.recoder_index >= 0:
            self.chinese_dict[self.recoder_index][1].configure(bg='pink')
        index = random.randint(0, 23)
        self.chinese_dict[index][1].configure(bg='red')
        self.recoder_index = index


if __name__ == '__main__':
    tiger_machine = tiger_machine()
    tiger_machine.create_windows()
