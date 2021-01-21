import pygame


def create_playing_field(screen):
    light_green_color = (0, 150, 0)
    dark_green_color = (0, 100, 0)
    size_block = 25
    head_margin = 50
    block_margin = 1
    count_box = 30
    for string in range(count_box):
        for column in range(count_box):
            if (string + column) % 2:
                color = dark_green_color
            else:
                color = light_green_color
            pygame.draw.rect(
                screen,
                color,
                [
                    20 + column * size_block + block_margin * (column + 1),
                    head_margin + 20 + string * size_block + block_margin * (string + 1),
                    size_block,
                    size_block
                ]
            )
