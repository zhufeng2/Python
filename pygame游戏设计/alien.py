# coding=utf-8
import sys
import pygame


def run_game():
    pygame.init()
    size = width, height = 600, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Alien Invasion')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    pygame.display.flip()


run_game()
