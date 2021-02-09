# coding=utf-8
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width))
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个储存子弹的编组,和外星人的编组
    bullets = Group()
    aliens = Group()
    # 创建一个外星人
    alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, aliens)
    while True:
        # 响应按键或鼠标的情况
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新屏幕
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove_internal(bullet)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)



run_game()
