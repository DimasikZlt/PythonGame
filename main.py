import sys
import pygame

pygame.init()

pygame.display.set_caption('Змейка')
head = pygame.image.load('Head.png')
snake_body = pygame.image.load('Body.png')
tale = pygame.image.load('Tail.png')

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

snake = [
    [size_block + block_margin, size_block * 3 + head_margin + block_margin * 3, 180],
    [size_block + block_margin, size_block * 2 + head_margin + block_margin * 2, 180],
    [size_block + block_margin, size_block + head_margin + block_margin, 180]
]

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
tick_time = 2


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
            elif event.key == pygame.K_LEFT and snake[0][2] != 270:
                snake[0][2] = 90
                break
            elif event.key == pygame.K_RIGHT and snake[0][2] != 90:
                snake[0][2] = 270
                break
            elif event.key == pygame.K_DOWN and snake[0][2] != 0:
                snake[0][2] = 180
                break
            elif event.key == pygame.K_UP and snake[0][2] != 180:
                snake[0][2] = 0
                break

    for index in range(len(snake) - 1, 0, -1):
        snake[index][0] = snake[index - 1][0]
        snake[index][1] = snake[index - 1][1]
        snake[index][2] = snake[index - 1][2]

    if snake[0][2] == 90:
        snake[0][0] -= 26
    elif snake[0][2] == 270:
        snake[0][0] += 26
    elif snake[0][2] == 180:
        snake[0][1] += 26
    elif snake[0][2] == 0:
        snake[0][1] -= 26
    if (snake[0][0] < min_size[0]
            or snake[0][1] < min_size[1]
            or snake[0][0] > max_size[0]
            or snake[0][1] > max_size[1]):
        sys.exit()

    screen.fill(screen_color)
    create_playing_field(screen)

    screen.blit(pygame.transform.rotate(head, snake[0][2]), (snake[0][0], snake[0][1]))
    for body in range(1, len(snake) - 1):
        screen.blit(
            pygame.transform.rotate(snake_body, snake[body][2]),
            (snake[body][0], snake[body][1])
        )
    screen.blit(pygame.transform.rotate(
        tale,
        snake[len(snake) - 1][2]),
        (snake[len(snake) - 1][0], snake[len(snake) - 1][1])
    )

    pygame.display.flip()
    clock.tick(tick_time)
