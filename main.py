import pygame
from GameConstants import *
from Soldier import Soldier
from Grenade import Grenade
from ItemBox import ItemBox
from HealthBar import HealthBar
from World import World

pygame.init()

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

#load images
bullet_img = pygame.image.load('img/icons/bullet.png').convert_alpha()
grenade_img = pygame.image.load('img/icons/grenade.png').convert_alpha()

#define font
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_bg():
	screen.fill(BG)
	pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))

#create sprite groups
bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
item_box_group = pygame.sprite.Group()
decoration_group = pygame.sprite.Group()
water_grup = pygame.sprite.Group()
exit_group = pygame.sprite.Group()


#create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)
#load in level data and create world
with open(f'level{LEVEL}_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='')
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_datap[x][y] = int(tile)
world = Wold()
player, health_bar = world.process_data(world_data, screen, bullet_group, water_group, decoration_group, enemy_group, item_box_group, exit_group)


#game loop/events
run = True
while run:

    clock.tick(FPS)

    #update background
    draw_bg()
    #draw world map
    world.draw(screen)

    #show player health
    health_bar.draw(player.health, screen)
    #show ammo
    draw_text('AMMO:', font, WHITE, 10, 35)
    for x in range(player.ammo):
        screen.blit(bullet_img, (90 + (x * 10), 40))
    draw_text('GRENADES:', font, WHITE, 10, 60)
    for x in range(player.grenades):
        screen.blit(grenade_img, (135 + (x * 15), 60))


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

    for enemy in enemy_group:
        enemy.ai(player)
        enemy.update()
        enemy.draw(screen)

    #update and draw groups
    bullet_group.update()
    grenade_group.update(player, enemy_group, explosion_group)
    explosion_group.update()
    item_box_group.update(player)
    decoration_group.update()
    water_group.update()
    exit_group.update()


    bullet_group.draw(screen)
    grenade_group.draw(screen)
    explosion_group.draw(screen)
    item_box_group.draw(screen)
    decoration_group.draw(screen)
    water_group.draw(screen)
    exit_group.draw(screen)

    #make entities take damage
    if pygame.sprite.spritecollide(player, bullet_group, False):
        if player.alive:
            player.health -= 10
            for bullet in bullet_group:
                bullet.kill()
    if pygame.sprite.spritecollide(enemy, bullet_group, False):
        if enemy.alive:
            enemy.health -= 25
            for bullet in bullet_group:
                bullet.kill()

    #events
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