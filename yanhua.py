import math
import random
import threading
import time
from math import sin, cos, pi, log
from tkinter import *
import re

# 烟花相关设置
Fireworks = []
maxFireworks = 8
CANVAS_WIDTH = 1080  # 画布的宽
CANVAS_HEIGHT = 600  # 画布的高
CANVAS_CENTER_X = CANVAS_WIDTH / 2  # 画布中心的X轴坐标
CANVAS_CENTER_Y = CANVAS_HEIGHT / 2  # 画布中心的Y轴坐标
IMAGE_ENLARGE = 12  # 放大比例
HEART_COLOR = "pink"  # 心的颜色


# 烟花类
class firework(object):
    def __init__(self, color, speed, width, height):
        self.radius = random.randint(2, 3)  # 粒子半径为2~3像素
        self.color = color  # 粒子颜色
        self.speed = speed  # speed是1.5-3.5秒
        self.status = 0  # 在烟花未爆炸的情况下，status=0；爆炸后，status>=1；当status>100时，烟花的生命期终止
        self.nParticle = random.randint(80, 100)  # 粒子数量
        self.center = [random.randint(0, width - 15), random.randint(0, height - 15)]  # 烟花随机中心坐标
        self.oneParticle = []  # 原始粒子坐标（100%状态时）
        self.rotTheta = random.uniform(-1, 2 * math.pi)  # 椭圆平面旋转角
        self.ellipsePara = [random.randint(30, 40), random.randint(20, 30)]  # 椭圆参数方程：x=a*cos(theta),y=b*sin(theta)

        theta = 2 * math.pi / self.nParticle
        for i in range(self.nParticle):
            t = random.uniform(-1.0 / 16, 1.0 / 16)  # 产生一个 [-1/16,1/16) 的随机数
            x, y = self.ellipsePara[0] * math.cos(theta * i + t), self.ellipsePara[1] * math.sin(
                theta * i + t)  # 椭圆参数方程
            xx, yy = x * math.cos(self.rotTheta) - y * math.sin(self.rotTheta), y * math.cos(
                self.rotTheta) + x * math.sin(self.rotTheta)  # 平面旋转方程
            self.oneParticle.append([xx, yy])

        self.curParticle = self.oneParticle[0:]  # 当前粒子坐标
        self.thread = threading.Thread(target=self.extend)  # 建立线程对象
