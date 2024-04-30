import pygame

SCREEN_WIDTH = 800

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

    def update(self):
        #move bullet
        self.rect.x += (self.__speed * self.direction)

        #check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > self.soldier.screen.get_width():
            self.kill()

        #check collision with characters
        if pygame.sprite.spritecollide(self.soldier, self.bullet_group, False):
            if self.soldier.alive and not self.is_enemy:
                self.soldier.health -= 5
                self.kill()