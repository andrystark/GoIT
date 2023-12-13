import pygame
pygame.init()


HEIGHT = 800

WIDTH = 1200

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
surf = pygame.Surface((150, 150))
playing = True

while playing:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

             playing = False
player_size = (20, 20)

player = pygame.Surface(player_size)
COLOR_WHITE = (255, 255, 255)  # Білий колір*

player.fill(COLOR_WHITE)
player_rect = player.get_rect()

main_display.blit(player, player_rect)
pygame.display.flip()
player_speed = [1, 1]
player_rect = player_rect.move(player_speed)
main_display.fill((0, 0, 0))
FPS = pygame.time.Clock()

FPS.tick(120)
if player_rect.bottom >= HEIGHT:

    player_speed = random.choice(([1, -1], [-1, -1]))
if player_rect.bottom >= WIDTH:

    player_speed = random.choice(([1, -1], [-1, -1]))


            
            
