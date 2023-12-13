import pygame 
import random
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

HEIGHT = 800
WIDTH = 1200

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
player_size = (20, 20)

player = pygame.Surface(player_size)
COLOR_WHITE = (255, 255, 255)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    keys = pygame.key.get_pressed()

    player_speed = 5

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(0, player_speed)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(0, -player_speed)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(-player_speed, 0)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_speed, 0)

    main_display.fill((0, 0, 0))
    main_display.blit(player, player_rect)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

# Закриття вікна та виход з програми при натисканні "X" на вікні
pygame.quit()
