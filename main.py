from random import randint
import sys
import pygame
import pygame_menu

pygame.init()

pygame.display.set_caption('Змейка')
screen = pygame.display.set_mode((830, 880))


def start_the_game():
    head = pygame.image.load('Image/Head.png')
    snake_body = pygame.image.load('Image/Body.png')
    tale = pygame.image.load('Image/Tail.png')
    apple_img = pygame.image.load('Image/Apple.png')
    bomb_img = pygame.image.load('Image/Bomb.png')
    amanita_img = pygame.image.load('Image/Amanita.png')
    banana_img = pygame.image.load('Image/Banana.png')
    RA_img = pygame.image.load('Image/Rainbow_apple.png')

    screen_color = (0, 0, 0)
    light_green_color = (0, 150, 0)
    dark_green_color = (0, 100, 0)

    size_block = 25
    head_margin = 50
    block_margin = 1
    count_box = 30
    score = 0

    font = pygame.font.Font(None, 72)

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
    apples = []
    bananas = []
    bombs = []
    amanitas = []
    rainbow_apple = []
    is_alive_rainbow_apple = True
    lists = (apples, bananas, bombs, amanitas, rainbow_apple)
    counts_elements = (10, 3, 2, 4, 1)

    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    speed = 2
    tick = 0

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

    def populating_lists(eat_list: list, count: int):
        while len(eat_list) < count:
            x = randint(1, 30) * (block_margin + size_block)
            y = randint(1, 30) * (block_margin + size_block) + head_margin
            if (
                    [x, y] not in apples
                    and [x, y] not in bananas
                    and [x, y] not in bombs
                    and [x, y] not in amanitas
                    and [x, y] != rainbow_apple
            ):
                eat_list.append([x, y])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_LEFT and snake[0][2] != 270:
                    snake[0][2] = 90
                    # break
                elif event.key == pygame.K_RIGHT and snake[0][2] != 90:
                    snake[0][2] = 270
                    # break
                elif event.key == pygame.K_DOWN and snake[0][2] != 0:
                    snake[0][2] = 180
                    # break
                elif event.key == pygame.K_UP and snake[0][2] != 180:
                    snake[0][2] = 0
                    # break

        for index in range(len(lists)):
            populating_lists(lists[index], counts_elements[index])

        if not is_alive_rainbow_apple:
            tick += 1
        if tick == 100:
            is_alive_rainbow_apple = True
            tick = 0

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

        if (
                snake[0][0] < min_size[0]
                or snake[0][1] < min_size[1]
                or snake[0][0] > max_size[0]
                or snake[0][1] > max_size[1]
        ):
            break

        for index in range(1, len(snake)):
            if snake[0][0] == snake[index][0] and snake[0][1] == snake[index][1]:
                break

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

        for apple in apples:
            if apple[0] == snake[0][0] and apple[1] == snake[0][1]:
                score += 1
                apples.remove(apple)
                snake.append([snake[len(snake) - 1][2], snake[len(snake) - 1][0], snake[len(snake) - 1][1]])

        for banana in bananas:
            if banana[0] == snake[0][0] and banana[1] == snake[0][1]:
                score += 3
                bananas.remove(banana)
                snake.append([snake[len(snake) - 1][2], snake[len(snake) - 1][0], snake[len(snake) - 1][1]])

        for amanita in amanitas:
            if amanita[0] == snake[0][0] and amanita[1] == snake[0][1]:
                score -= 5
                if score < 0:
                    score = 0
                amanitas.remove(amanita)

        for bomb in bombs:
            if bomb[0] == snake[0][0] and bomb[1] == snake[0][1]:
                break

        if rainbow_apple[0][0] == snake[0][0] and rainbow_apple[0][1] == snake[0][1]:
            score += 10
            is_alive_rainbow_apple = False
            snake.append([snake[len(snake) - 1][2], snake[len(snake) - 1][0], snake[len(snake) - 1][1]])

        for apple in apples:
            screen.blit(apple_img, (apple[0], apple[1]))
        for banana in bananas:
            screen.blit(banana_img, (banana[0], banana[1]))
        for bomb in bombs:
            screen.blit(bomb_img, (bomb[0], bomb[1]))
        for amanita in amanitas:
            screen.blit(amanita_img, (amanita[0], amanita[1]))
        if is_alive_rainbow_apple:
            screen.blit(RA_img, (rainbow_apple[0][0], rainbow_apple[0][1]))

        if speed < 30:
            if score // 10 >= speed:
                speed += 1

        text = font.render(f"Score: {score}", True, (0, 100, 0))
        screen.blit(text, (20, 20))
        pygame.display.flip()
        clock.tick(speed)


menu = pygame_menu.Menu(750, 750, 'Welcome',
                        theme=pygame_menu.themes.THEME_BLUE)

menu.add_text_input('Name :', default='Player 1')
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
