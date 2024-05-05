import pygame

from GameConstants import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, soldier, bullet_group, is_enemy):
        super().__init__()
        self.__speed = 10
        self.image = pygame.image.load('img/icons/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.soldier = soldier
        self.bullet_group = bullet_group
        self.is_enemy = is_enemy

    def update(self, SCREEN_SCROLL):
        #move bullet
        self.rect.x += (self.__speed * self.direction) + SCREEN_SCROLL

        #check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > self.soldier.screen.get_width():
            self.kill()