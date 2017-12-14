# 用于奖励的掉落
import pygame
from pygame.sprite import Sprite
import random


class Award(Sprite):
    def __init__(self, settings, screen, block):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.flag = False
        if random.randint(0, 1) == 0:
            self.image = pygame.image.load('images/pic1.png')
            self.flag = True
        else:
            self.image = pygame.image.load('images/pic2.png')
            self.flag = False
        self.rect = self.image.get_rect()
        self.screen = screen.get_rect()
        self.x = float(block.rect.left)
        self.y = float(block.rect.top)
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, *args):
        self.rect.y = self.rect.y + self.settings.aware_down_speed
