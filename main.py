import sys
import pygame
from playing_field import create_playing_field

pygame.init()

screen_color = (0, 0, 0)

screen_size = (820, 870)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Змейка')
head = pygame.image.load('Head.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(screen_color)
    create_playing_field(screen)
    screen.blit(head, (410, 435))
    pygame.display.flip()
