from os import path
import pygame
import time
import mido  # 导入头文件
from pygame.locals import *  # 导入设置文件


class Set:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.color = (54, 52, 51)
        self.falling_rate = 0.30  # 每多少帧向下落一像素
        self.whitekeyheight = 120  # 键盘上的黑白键长宽
        self.blackkeyheight = 85
        self.whitekeywidth = 36
        self.blackkeywidth = 24
        self.baseFPS = 60
        self.font = "simkai.ttf"


sets = Set()


class Note:
    def __init__(self, tone, velo, time, long):
        self.tone = tone
        self.velo = velo
        self.time = time  # 按下时间
        self.long = long  # 时长
        if self.tone % 12 in (1, 3, 5, 6, 8, 10, 0):
            self.worb = 1  # white/black black=0 white=1
        else:
            self.worb = 0


def keyboard_init():
    keyboard = {}  # 字典，包含所有琴键的矩形对象
    whitenum = 0
    blacknum = 0  # 正在处理第几个黑/白键
    black_position = -2-sets.whitekeywidth
    # 正在处理黑键位置
    for i in range(1, 61):
        if i % 12 in (1, 3, 5, 6, 8, 10, 0):  # 是白键
            whitenum += 1
            keyboard[i] = (Rect(-26 + whitenum * sets.whitekeywidth, sets.height-sets.whitekeyheight,
                                sets.whitekeywidth, sets.whitekeyheight), 1)  # 后面一个数black=0,white=1
        else:
            blacknum += 1
            if blacknum % 5 in (3, 1):
                black_position += sets.whitekeywidth*2
            else:
                black_position += sets.whitekeywidth
            keyboard[i] = (Rect(black_position, sets.height-sets.whitekeyheight,
                                sets.blackkeywidth, sets.blackkeyheight), 0)
    return keyboard

