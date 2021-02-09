import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        # ��ʼ��������λ�ò�������ʼλ��
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # ����������ͼ�񣬲�����rectͼ��
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # ÿ�������˵����λ������Ļ������
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # �洢�����˵�׼ȷλ��

        self.x = float(self.rect.x)
    

    # ��ָ��λ�û���������
    def blitme(self):
        self.screen.blit(self.image, self.rect)