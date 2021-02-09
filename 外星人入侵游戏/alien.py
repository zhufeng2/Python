import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        # 初始化外星人位置并设置起始位置
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置rect图像
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人的最初位置在屏幕的中心
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置

        self.x = float(self.rect.x)
    

    # 在指定位置绘制外星人
    def blitme(self):
        self.screen.blit(self.image, self.rect)