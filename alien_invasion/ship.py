#飞船的特性，绘制以及特性更新
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        super().__init__()

        #初始化飞船并设置初始位置
        self.screen = screen

        #加载飞船图像，并获取外接矩形
        self.image=pygame.image.load('images/fly_object.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        #实例化设置
        self.ai_settings=ai_settings

        #移动flag
        self.moving_right=False
        self.moving_left=False

        #将新飞船放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom


        #改变速度初始化
        self.center=float(self.rect.centerx)

    def update(self):
        if self.moving_right and self.rect.centerx<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.centerx>0:
            self.center-=self.ai_settings.ship_speed_factor

        self.rect.centerx=self.center

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        #y轴不用改变，没有移动
        self.center=self.screen_rect.centerx