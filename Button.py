import pygame

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Set the position of the button
        self.clicked = False

    def draw(self, surface):
        action = False
        # Get mouse position
        position = pygame.mouse.get_pos()
        # Check if mouseover and clicked conditions
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
        else:
            self.clicked = False  # Reset clicked state if not hovering over the button

        # Draw button
        surface.blit(self.image, self.rect)

        return action