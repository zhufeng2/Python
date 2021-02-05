# coding=utf-8
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
import alien_invasion as ai


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.height, ai_settings.width))
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    while True:
        # 响应按键或鼠标的情况
        gf.check_events(ship)
        # 更新屏幕
        ship.update()
        ai.update_screen(ai_settings, screen, ship)


run_game()
