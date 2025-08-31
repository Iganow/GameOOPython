import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Cria uma superfície pequena representando a bala (um retângulo)
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 0))  # Amarelo
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_y = -10

    def update(self, *args):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()
