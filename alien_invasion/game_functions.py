#飞船功能（左右移动）的实现；屏幕显示的刷新
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #按键按下事件
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
       fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event,ship):
    #按键抬起事件
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,stats,ship,aliens,bullets,play_button,sb):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #如果事件是按键按下
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
    #按键抬起表示停止
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
    #鼠标点击开始按钮
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,ship,aliens,bullets,sb,play_button,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,ship,aliens,bullets,sb,play_button,mouse_x,mouse_y):
    """点击Play开始游戏"""
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)
        #先要清楚历史记录
        stats.reset_stats()
        stats.game_active=True
        #重置计分图像
        sb.prep_score()
        sb.prep_highest_score()
        sb.prep_level()
        sb.prep_ships()
        #清空外星人，子弹；创建外形人，飞船居中
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update()

    #删除已超出子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    # 检查是否子弹击中外星人，groupcollide方法返回字典，key是子弹，value是alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if  collisions:
        for aliens in collisions.values():
            stats.score+=ai_settings.alien_points*len(aliens)
            sb.prep_score()
        check_highest_score(stats,sb)
     # 已有的全部击落后创建新的
    if len(aliens) == 0:
        bullets.empty()
        stats.level+=1
        sb.prep_level()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings,screen,ship,bullets):
    # 创建新子弹，并加入已有子弹组中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings,stats,screen,sb,ship,aliens,bullets,play_button):
    #更新屏幕上的图，并切换到新屏幕
    screen.fill(ai_settings.bg_color)

    #绘制子弹,bullets.sprites()返回的是一个列表，包含bullets中的所有sprite

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    sb.show_score()

    #如果处于非活动状态就绘制button
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def get_numbrer_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y=ai_settings.screen_height-3*alien_height-ship_height
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    #创建一个外星人并放在当前行

    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y= alien.rect.height+2*row_number*alien.rect.height
    aliens.add(alien)


def create_fleet(ai_settings,screen,ship,aliens):
    #创建外星人群
    #创建一个外星人，并计算可容纳多少个外星人，间距为宽度
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_numbrer_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    #如果有外星人在边缘，则改变方向
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites() :
        alien.rect.y+=ai_settings.alien_drop_speed
    ai_settings.fleet_direction*=-1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """飞船被撞到"""
    if stats.ship_left:
        #生命-1
        stats.ship_left-=1
        sb.prep_ships()
        #清空外星人与子弹
        aliens.empty()
        bullets.empty()
        #创建新的外星人
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #暂停
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """检查是否有外星人到了底端"""
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            #飞船相当于被撞到
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #若果飞船与外星人相撞，collideany没有相撞的时候返回的是none
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

def check_highest_score(stats,sb):
    """检查最新得分是否为最高分"""
    if stats.highest_score<stats.score:
        stats.highest_score=stats.score
        sb.prep_highest_score()


