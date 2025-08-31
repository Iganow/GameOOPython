import pygame
import sys
from player import Player
from enemy import Enemy
from background import Background

pygame.init()

# Settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Demo 🚀")
clock = pygame.time.Clock()

# Game states
MENU = "menu"
PLAYING = "playing"
GAME_OVER = "game_over"


def draw_text(text, size, color, x, y, center=True):
    font = pygame.font.SysFont(None, size)
    render = font.render(text, True, color)
    rect = render.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(render, rect)


def game_loop():
    state = MENU
    score = 0

    # Groups
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    background = Background(SCREEN_WIDTH, SCREEN_HEIGHT)
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    all_sprites.add(player)

    for _ in range(5):
        enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
        all_sprites.add(enemy)
        enemies.add(enemy)

    running = True
    while running:
        clock.tick(60)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if state == MENU and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = PLAYING

            elif state == GAME_OVER and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # restart
                    return True

            elif state == PLAYING and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot(all_sprites, bullets)

        # Update & Draw
        if state == MENU:
            background.draw(screen)
            draw_text("SLIME DEFENDER", 48, (255, 255, 255), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
            draw_text("Aperte Espaço", 28, (200, 200, 200), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        elif state == PLAYING:
            all_sprites.update(SCREEN_WIDTH)

            # Bullet x Enemy
            hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for _ in hits:
                score += 10
                enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                all_sprites.add(enemy)
                enemies.add(enemy)

            # Enemy x Player
            if pygame.sprite.spritecollide(player, enemies, False):
                state = GAME_OVER

            background.draw(screen)
            all_sprites.draw(screen)
            draw_text(f"Score: {score}", 28, (255, 255, 255), 10, 10, center=False)

        elif state == GAME_OVER:
            background.draw(screen)
            draw_text("GAME OVER", 48, (255, 50, 50), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
            draw_text(f"Pontuação: {score}", 32, (255, 255, 255), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text("Para jogar de novo, aperte R", 24, (200, 200, 200), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5)

        pygame.display.flip()

    return False


# Loop with restart support
while True:
    restart = game_loop()
    if not restart:
        break

pygame.quit()
sys.exit()

