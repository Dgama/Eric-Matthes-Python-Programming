import pygame
#sprite可以将游戏中相关元素编组，从而可以操作组中的所有元素
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):

        super().__init__()
        self.screen=screen

        #利用像素创建子弹，并将子弹初始位置改变
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        #子弹位置参数
        self.y = float(self.rect.y)

    def update(self):
        #更新子弹的位置
        self.y -= self.speed_factor

        self.rect.y = self.y

    def draw_bullet(self):
        #绘制子弹
        pygame.draw.rect(self.screen,self.color,self.rect)
