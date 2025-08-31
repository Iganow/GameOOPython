import pygame

class Background:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("assets/background.png").convert()
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
