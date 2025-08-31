import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        # Carrega o sprite do inimigo
        self.image = pygame.image.load("assets/enemy.png").convert_alpha()
        # Reduz o tamanho do sprite (menor)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

        # posição inicial aleatória
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)

        # velocidade mais lenta
        self.speed_y = random.randint(1, 3)

        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, *args):
        self.rect.y += self.speed_y
        if self.rect.top > self.screen_height:
            # reposiciona no topo
            self.rect.x = random.randint(0, self.screen_width - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.randint(1, 3)

