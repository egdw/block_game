# -*- coding: utf-8 -*-
import sys
import pygame
from setting import Settings
from Controller import Controller
import game_function as gf
from  pygame.sprite import Group
from block import Block
import random


def run_game():
    settings = Settings()
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    controller = Controller(screen, settings)
    blocks = Group()
    for x in range(settings.block_count):
        block = Block(settings, screen)
        ran = random.randint(0, 100)
        if ran < settings.destory_occurrence_rate:
            # 15 % 的概率生成无法破坏的砖块
            block.destory = False
            block.color = (120, 120, 120)
        blocks.add(block)
    pygame.display.set_caption("block_game")
    group = Group()
    # 存放控制器的iterator
    controllers = Group()
    controllers.add(controller)
    # 进行循环判断当前的状态
    while True:
        gf.check_event(controller, group, settings, screen)
        controller.update()
        gf.update_screen(settings, screen, controller, group, blocks)
        group.update()
        gf.update_block(group, blocks, controllers)


run_game()
