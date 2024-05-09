import unittest
from Soldier import Soldier
from Bullet import Bullet
import pygame
from GameConstants import *

class TestSoldier(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bullet_group = pygame.sprite.Group()
        self.obstacle_list = []
        self.soldier = Soldier('char_type', TILE_SIZE * 5, TILE_SIZE * 5, 1.65, SPEED, AMMO, GRENADES, self.bullet_group, self.screen, False, self.obstacle_list)


    def test_init(self):
        self.assertIsInstance(self.soldier, pygame.sprite.Sprite)
        self.assertEqual(self.soldier.char_type, 'char_type')
        self.assertEqual(self.soldier.speed, 5)
        self.assertEqual(self.soldier.ammo, 10)
        self.assertEqual(self.soldier.grenades, 5)
        self.assertEqual(self.soldier.health, 100)
        self.assertEqual(self.soldier.max_health, 100)

    def test_update(self):
        self.soldier.update()
        self.assertEqual(self.soldier.shoot_cooldown, 0)

    def test_move(self):
        self.soldier.move(True, False)
        self.assertEqual(self.soldier.flip, True)
        self.assertEqual(self.soldier.direction, -1)

    def test_shoot(self):
        self.soldier.shoot()
        self.assertEqual(self.soldier.shoot_cooldown, 20)
        self.assertEqual(self.soldier.ammo, 9)

    def test_ai(self):
        player = Soldier('char_type', 100, 100, 1, 5, 10, 5, self.bullet_group, self.screen, False, self.obstacle_list)
        self.soldier.ai(player)
        self.assertEqual(self.soldier.idling, True)

    def test_update_animation(self):
        self.soldier.update_animation()
        self.assertEqual(self.soldier.frame_index, 1)

    def test_update_action(self):
        self.soldier.update_action(1)
        self.assertEqual(self.soldier.action, 1)

    def test_check_alive(self):
        self.soldier.health = 0
        self.soldier.check_alive()
        self.assertEqual(self.soldier.alive, False)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()