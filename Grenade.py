import pygame
from Bullet import Bullet

GRAVITY = 0.75
SCREEN_WIDTH = 800  # Define SCREEN_WIDTH here

class Grenade(Bullet):
    def __init__(self, x, y, direction, soldier, bullet_group, is_enemy):
        super().__init__(x, y, direction, soldier, bullet_group, is_enemy)
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = pygame.image.load('img/icons/grenade.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        # check collision with floor
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.speed = 0

        # check collision with walls
        if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
            self.direction *= -1
            dx = self.direction * self.speed

        # update grenade position
        self.rect.x += dx
        self.rect.y += dy

        # decrement timer
        self.timer -= 1
        if self.timer <= 0:
            # explode the grenade
            self.kill()