import pygame
import os
import random
from Bullet import Bullet

from GameConstants import *

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, grenades, bullet_group, screen, is_enemy, obstacle_list):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_group = bullet_group
        self.is_enemy = is_enemy
        self.screen = screen
        self.alive = True
        self.char_type = char_type
        self.__speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.shoot_cooldown = 0
        self.grenades = grenades
        self.health = 100
        self.max_health = self.health
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.obstacle_list = obstacle_list
        #ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150 , 20)
        self.idling = False
        self.idling_counter = 0

        #load all images for the player
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            #reset temporary list of images
            temp_list = []
            #count number of files in the folder
            num_of_frames = len(os.listdir(f'img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.check_alive()
        #update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        # update animation
        self.update_animation()

    def move(self, moving_left, moving_right):
        #reset movement variables
        dx = 0
        dy = 0

        #assing movement variables
        if moving_left:
            dx = -self.__speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.__speed
            self.flip = False
            self.direction = 1

        #jumping
        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        #apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        #check for collision with edges of screen
        if self.rect.left + dx < 0:
            dx = 0
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = 0
        if self.rect.top + dy < 0:
            dy = 0
        if self.rect.bottom + dy > SCREEN_HEIGHT:
            dy = 0

        #check for collision with tiles
        for tile in self.obstacle_list:
            #check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            #check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if below the ground i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                #check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction, self, bullet_group=self.bullet_group, is_enemy=self.is_enemy)
            self.bullet_group.add(bullet)
            self.ammo -= 1

    def ai(self, player):
        if self.alive and player.alive:
            if self.idling == False and random.randint(1, 250) == 1:
                self.update_action(0)#0: idle
                self.idling = True
                self.idling_counter = 100
            #check if the ai is near player
            if self.vision.colliderect(player.rect):
                #stop running and face the player
                self.update_action(0)#0: idle
                self.shoot()
            else:
                if self.idling == False:
                    if self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)#1: run
                    self.move_counter += 1
                    #update ai vision as enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)
                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False
        elif player.alive == False:
            self.update_action(0)#0: idle

    def update_animation(self):
        #update animation
        ANIMATION_COOLDOWN = 100
        #update image depending on current frame
        if self.frame_index < len(self.animation_list[self.action]):
            self.image = self.animation_list[self.action][self.frame_index]
        else:
            self.frame_index = 0
            self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        #check if the new action is different from before
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)