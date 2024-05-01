import pygame
from Bullet import Bullet
from Explosion import Explosion

from GameConstants import *

class Grenade(Bullet):
    def __init__(self, x, y, direction, soldier, bullet_group, is_enemy, obstacle_list):
        super().__init__(x, y, direction, soldier, bullet_group, is_enemy)
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = pygame.image.load('img/icons/grenade.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.obstacle_list = obstacle_list
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, player, enemy_group, explosion_group):
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        # check collision with floor
        #check for collision
        for tile in self.obstacle_list:
            #check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                self.direction *= -1
                dx = self.direction * self.speed
            #check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                self.speed = 0
                #check if below the ground i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                #check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom

        # update grenade position
        self.rect.x += dx
        self.rect.y += dy

        # decrement timer
        self.timer -= 1
        if self.timer <= 0:
            # explode the grenade
            self.kill()
            explosion = Explosion(self.rect.x, self.rect.y, 2)
            explosion_group.add(explosion)
            if abs(self.rect.centerx - player.rect.centerx) < TILE_SIZE * 3 and \
                abs(self.rect.centery - player.rect.centery) < TILE_SIZE * 3:
                player.health -= 50
            for enemy in enemy_group:
                if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 3 and \
                abs(self.rect.centery - enemy.rect.centery) < TILE_SIZE * 3:
                    enemy.health -= 50