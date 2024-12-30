import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect the Stars!")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Player speed
PLAYER_SPEED = 5

# Player
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player = pygame.Rect(player_x, player_y, player_size, player_size)

# Star
star_size = 30
star = pygame.Rect(random.randint(0, WIDTH - star_size), random.randint(0, HEIGHT - star_size), star_size, star_size)

# Score counter
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED

    # Restrict player movement within screen boundaries
    player.x = max(0, min(WIDTH - player_size, player.x))
    player.y = max(0, min(HEIGHT - player_size, player.y))

    # Check collision between player and star
    if player.colliderect(star):
        score += 1
        star.x = random.randint(0, WIDTH - star_size)
        star.y = random.randint(0, HEIGHT - star_size)

    # Draw player and star
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, YELLOW, star)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
