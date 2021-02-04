import pygame

def run_game():
    # 初始化pygame
    pygame.init()

    # 初始化游戏屏幕、游戏名设置，屏幕大小设置时要加括号
    ai_settings = Settings() # 初始设置类的实例化
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button,
            ship, aliens, bullets)


run_game()
