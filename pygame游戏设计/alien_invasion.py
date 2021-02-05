import pygame


def update_screen(ai_settings, screen, ship):
    # 每次循环都重叠屏幕
    screen.fill(ai_settings.bg_color)
    # 指定位置绘制出飞船
    ship.blitme()
    pygame.display.flip()
