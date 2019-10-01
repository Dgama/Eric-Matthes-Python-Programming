#主程序，包含循环代码，将各部分联系到一起，并绘制在主screen上
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from Scoreboard import Scoreboad
from button import Button

#一个编组，用于存储所有的有效子弹，以便同时管理
from pygame.sprite import Group

def run_game():
    #创建屏幕对象
    pygame.init()

    ai_settings=Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    pygame.display.set_caption("alien_invasion")

    play_button=Button(ai_settings,screen,"Play")

    stats=GameStats(ai_settings)

    sb=Scoreboad(ai_settings,screen,stats)

    ship=Ship(ai_settings,screen)

    bullets=Group()
    aliens=Group()

#创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #开始游戏主循环
    while True:

        gf.check_events(ai_settings,screen,stats,ship,aliens,bullets,play_button,sb)
        if stats.game_active:
            #每次循环都重绘屏幕
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb)

        gf.update_screen(ai_settings,stats,screen,sb,ship,aliens,bullets,play_button)

run_game()


