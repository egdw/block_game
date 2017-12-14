# 主要的球类 也就是击打出去的球
import pygame
from pygame.sprite import Sprite
import random


class Ball(Sprite):
    def __init__(self, settings, screen, controller):
        super().__init__()
        self.screen = screen
        # 转向速度
        self.settings = settings
        self.right = False
        self.turn_speed = 0 - settings.ball_speed
        self.controller = controller
        self.rect = pygame.Rect(0, 0, settings.ball_width, settings.ball_height)
        self.rect.centerx = controller.rect.centerx
        self.rect.top = controller.rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.color = settings.ball_color
        self.speed = settings.ball_speed

    def update(self, *args):
        self.y -= self.speed
        self.x += self.turn_speed
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def make_turn(self, want):
        # self.speed = 0 - self.speed
        # 方向转换.之后进行角度的转换
        # if random.randint(0, 1) == 0:
        #     self.turn_speed = self.speed
        # else:\
        if want == 1:
            self.turn_speed = 0 - self.turn_speed
        elif want == 0:
            self.speed = 0 - self.speed
            self.turn_speed = 0 - self.turn_speed
        elif want == 2:
            self.speed = 0 - self.speed
