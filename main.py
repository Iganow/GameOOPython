import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA = 600
ALTURA = 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Demo - Nave Espacial 🚀")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Classe Jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 20))
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA // 2
        self.rect.bottom = ALTURA - 10
        self.velocidade = 5

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < LARGURA:
            self.rect.x += self.velocidade

    def atirar(self):
        tiro = Tiro(self.rect.centerx, self.rect.top)
        todos_sprites.add(tiro)
        tiros.add(tiro)

# Classe Inimigo
class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(VERMELHO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.velocidadey = random.randint(2, 6)

    def update(self):
        self.rect.y += self.velocidadey
        if self.rect.top > ALTURA:
            self.rect.x = random.randint(0, LARGURA - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.velocidadey = random.randint(2, 6)

# Classe Tiro
class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocidadey = -7

    def update(self):
        self.rect.y += self.velocidadey
        if self.rect.bottom < 0:
            self.kill()

# Criar grupos de sprites
todos_sprites = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
tiros = pygame.sprite.Group()

# Criar jogador
jogador = Jogador()
todos_sprites.add(jogador)

# Criar inimigos
for _ in range(5):
    inimigo = Inimigo()
    todos_sprites.add(inimigo)
    inimigos.add(inimigo)

# Loop principal
pontos = 0
rodando = True
while rodando:
    clock.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jogador.atirar()

    # Atualizações
    todos_sprites.update()

    # Colisão tiro x inimigo
    colisao = pygame.sprite.groupcollide(inimigos, tiros, True, True)
    for _ in colisao:
        pontos += 10
        inimigo = Inimigo()
        todos_sprites.add(inimigo)
        inimigos.add(inimigo)

    # Colisão jogador x inimigo
    if pygame.sprite.spritecollide(jogador, inimigos, False):
        print("💥 Game Over! Pontos:", pontos)
        rodando = False

    # Desenho
    TELA.fill(PRETO)
    todos_sprites.draw(TELA)

    # Pontuação
    fonte = pygame.font.SysFont(None, 36)
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    TELA.blit(texto, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()