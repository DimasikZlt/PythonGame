import sys
import pygame

pygame.init()

screen_color = (255, 255, 255)

screen_size = (800, 800)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Змейка')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(screen_color)
    pygame.display.flip()
