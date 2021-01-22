import sys
import pygame

pygame.init()

pygame.display.set_caption('Змейка')
head = pygame.image.load('Head.png')
screen_color = (0, 0, 0)
light_green_color = (0, 150, 0)
dark_green_color = (0, 100, 0)
size_block = 25
head_margin = 50
block_margin = 1
count_box = 30
screen_size = (
    size_block * count_box + 2 * size_block + block_margin * count_box,
    size_block * count_box + 2 * size_block + block_margin * count_box + head_margin
)
min_size = (size_block + block_margin, size_block + head_margin)
max_size = (screen_size[0] - size_block, screen_size[1] - size_block - 1)
x = size_block + block_margin
y = size_block + head_margin
rotate = 0
screen = pygame.display.set_mode(screen_size)


def create_playing_field(game_screen):
    for string in range(count_box):
        for column in range(count_box):
            if (string + column) % 2:
                color = dark_green_color
            else:
                color = light_green_color
            pygame.draw.rect(
                game_screen,
                color,
                [
                    size_block + column * size_block + block_margin * (column + 1),
                    head_margin + size_block + string * size_block + block_margin * (string + 1),
                    size_block,
                    size_block
                ]
            )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_LEFT:
                x -= 26
                rotate = 90
            elif event.key == pygame.K_RIGHT:
                x += 26
                rotate = 270
            elif event.key == pygame.K_DOWN:
                y += 26
                rotate = 180
            elif event.key == pygame.K_UP:
                y -= 26
                rotate = 0
    if x < min_size[0] or y < min_size[1] or x > max_size[0] or y > max_size[1]:
        sys.exit()
    screen.fill(screen_color)
    create_playing_field(screen)
    screen.blit(pygame.transform.rotate(head, rotate), (x, y))
    pygame.display.flip()
