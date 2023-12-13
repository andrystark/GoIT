import pygame
import random  # Додавання модуля random для використання функції random.choice

pygame.init()

HEIGHT = 800
WIDTH = 1200

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
player_size = (20, 20)

player = pygame.Surface(player_size)
COLOR_WHITE = (255, 255, 255)  # Білий колір*

player.fill(COLOR_WHITE)
player_rect = player.get_rect()

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    # Оновлення позиції гравця
    player_rect = player_rect.move([1, 1])  # Змінено на рух вправо та вниз

    # Обробка переходу гравця на протилежний бік, якщо він виходить за межі вікна
    if player_rect.bottom >= HEIGHT or player_rect.top <= 0:
        player_speed = random.choice(([1, 1], [-1, 1]))  # Змінено на зміну напрямку вгору та вниз

    if player_rect.right >= WIDTH or player_rect.left <= 0:
        player_speed = random.choice(([1, 1], [1, -1]))  # Змінено на зміну напрямку вправо та вліво

    main_display.fill((0, 0, 0))
    main_display.blit(player, player_rect)

    pygame.display.flip()

    pygame.time.Clock().tick(120)
