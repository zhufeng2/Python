# coding=utf-8
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.height, ai_settings.width))
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个储存子弹的编组
    bullets = Group()
    while True:
        # 响应按键或鼠标的情况
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新屏幕
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)
        # 删除已经消失的子弹


run_game()
