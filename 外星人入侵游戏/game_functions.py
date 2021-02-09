import pygame
import sys
from bullet import Bullet
from settings import Settings
from alien import Alien

def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹并将其加入到编组bullets中
        if len(bullets) <= ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add_internal(new_bullet)
    elif event.key == pygame.K_q:
            sys.exit()


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


# 这里面的key和type注意区分，对键盘的行为进行判断
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship,alien, bullets):
    # 每次循环都重叠屏幕
    screen.fill(ai_settings.bg_color)
    # 指定位置绘制出飞船
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    # 更新子弹的位置，并删除已经消失的子弹
    bullets.update()
    # 删除已经消失的子弹


def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width-2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))

    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width+2*alien_width*alien_number
        alien.rect.x = alien.x
        aliens.add_internal(alien)




