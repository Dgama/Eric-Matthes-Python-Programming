import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboad():

    def __init__(self,ai_settings,screen,stats):
        """初始化得分涉及的属性"""

        self.screen=screen
        self.ai_settigns=ai_settings
        self.stats=stats
        self.screen_rect=screen.get_rect()

        #得分信息的字体设置
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)

        #准备初始得分图像
        self.prep_score()
        self.prep_highest_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分转化为渲染的图像"""
        #近似到整数倍
        rounded_score=int(round(self.stats.score,-1))
        #格式化
        score_str="Score: "+"{:,}".format(rounded_score)

        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settigns.bg_color)

        #将得分放在右上角
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def prep_highest_score(self):
         """将最高分转化为渲染的图像"""
         # 近似到整数倍
         highest_rounded_score = int(round(self.stats.highest_score, -1))
         # 格式化
         highest_score_str = "Highest score: "+"{:,}".format(highest_rounded_score)

         self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.ai_settigns.bg_color)

         # 将最高分放在右上角
         self.highest_score_image_rect = self.highest_score_image.get_rect()
         self.highest_score_image_rect.centerx = self.screen_rect.centerx
         self.highest_score_image_rect.top = self.screen_rect.top

    def prep_level(self):
        """将等级转化为渲染的图像"""
        level_str = "level: "+str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_settigns.bg_color)

        # 将等级放在右上角
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom+10

    def prep_ships(self):
        """显示还剩多少飞船"""
        self.ships=Group()
        for ship_number in range(self.stats.ship_left):
            ship=Ship(self.ai_settigns,self.screen)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上方显示分数"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.highest_score_image,self.highest_score_image_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

