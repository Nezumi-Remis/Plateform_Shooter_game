import pygame
from Soldier import Soldier
from Grenade import Grenade


pygame.init()

#define game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
GRAVITY = 0.75
TILE_SIZE = 40

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Platformer Shooter')

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define player action variables
moving_left = False
moving_right = False
shoot = False
grenade = False
grenade_thrown = False

#define colours
BG = (144, 201, 120)
RED = (255, 0, 0)

def draw_bg():
	screen.fill(BG)
	pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))

#create sprite groups
bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

player = Soldier('player', 200, 200, 3, 5, 20, 5, bullet_group, screen, False)
enemy = Soldier('enemy', 400, 200, 3, 5, 20, 0, bullet_group, screen, True)
enemy_group.add(enemy)

#game loop/events
run = True
while run:

    clock.tick(FPS)

    draw_bg()

    #update player actions
    if player.alive:
        #shoot bullets
        if shoot:
            player.shoot()
        #throw grenade
        elif grenade and player.grenades > 0 and grenade_thrown == False:
            grenade = Grenade(player.rect.centerx + (0.5 * player.rect.size[0] * player.direction),\
                  player.rect.top, player.direction, player, bullet_group, False)
            grenade_group.add(grenade)
            player.grenades -= 1
            grenade_thrown = True
        if player.in_air:
            player.update_action(2)#2: jump
        elif moving_left or moving_right:
            player.update_action(1)#1: run
        else:
            player.update_action(0)#0: idle
        player.move(moving_left, moving_right)

    player.update()
    player.draw(screen)

    enemy.update()
    enemy.draw(screen)

    #update and draw groups
    bullet_group.update()
    grenade_group.update(player, enemy_group, explosion_group)
    explosion_group.update()
    bullet_group.draw(screen)
    grenade_group.draw(screen)
    explosion_group.draw(screen)

    #make entities take damage
    if pygame.sprite.spritecollide(enemy, bullet_group, False):
        if enemy.alive:
            enemy.health -= 25
            for bullet in bullet_group:
                bullet.kill()
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_q:
                grenade = True
            if event.key == pygame.K_w and player.alive:
                player.jump = True
            if event.key == pygame.K_ESCAPE:
                run = False
            
        #keivoard button realesed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_q:
                grenade = False
                grenade_thrown = False


    pygame.display.update()

pygame.quit()