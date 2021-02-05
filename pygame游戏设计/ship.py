import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        # 初始化位置并设置其初始位置
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船得图形并且获得其外界矩形
        self.image = pygame.image.load('images/ship.bmp')
        # 获得上面定义得图片得rect
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘飞船置于屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

    # 移动标志
    def update(self):
        # 比较运算符的优先顺序大于逻辑运算符
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据self.center更新前面的值
        self.rect.centerx = self.center

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
