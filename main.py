import pygame 
import random
from pygame.constants import QUIT, USEREVENT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

HEIGHT = 600
WIDTH = 1200

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
player_size = (20, 20)
bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))

bg_X1 = 0

bg_X2 = bg.get_width()

bg_move = 3

player = pygame.Surface(player_size)
COLOR_WHITE = (255, 255, 255)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()

enemy_size = (30, 30)
COLOR_BLUE = (0, 0, 255)

enemies = []
score = 0

CREATE_ENEMY = USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1000)  # Every second, create a new enemy

FONT = pygame.font.SysFont('Verdana', 20)

def create_enemy():
    enemy = pygame.Surface(enemy_size)
    enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
    enemy_move = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_move]

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

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

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

        # Check collision with enemies
        if player_rect.colliderect(enemy[1]):
            playing = False

    # Display score
    main_display.blit(bg, (0, 0))

    # Check if player collects bonuses (you need to add bonus handling code)
    # if player_rect.colliderect(bonus[1]):
    #     score += 1
    #     bonuses.pop(bonuses.index(bonus))  

    # Check if enemies go off the screen
    for enemy in enemies[:]:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
    # main_display.fill(COLOR_BlACK)

        bg_X1 -= bg_move

    bg_X2 -= bg_move

    main_display.blit(bg, (bg_X1, 0))

    main_display.blit(bg, (bg_X2, 0))        

    pygame.display.flip()

    pygame.time.Clock().tick(60)

# Close the window and exit the program when the "X" is clicked
pygame.quit()
