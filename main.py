import pygame
from Soldier import Soldier

pygame.init()

#screen parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Platformer Shooter')

player = Soldier(200, 200, 3)

#game loop/events
run = True
while run:


    player.draw(screen)

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        
        pygame.display.update()

pygame.quit()