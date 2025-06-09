import pygame
from player import Player
from level import load_level
from index import WIDTH, HEIGHT, TILE_SIZE, WHITE, BLACK

pygame.init()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Quest - Two Players")

# Load the background image
background = pygame.image.load("images/background.jpg")  # Ensure "background.jpg" is inside the images folder
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Resize to match the screen

# Load the level
level = load_level("levels/level1.txt")
blocks = []
player1 = None
player2 = None

# Place the players based on level data
for y, row in enumerate(level):
    for x, tile in enumerate(row):
        if tile == "X":  # Platform blocks
            # Temporary block (empty) for now
            blocks.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        elif tile == "P":
            player1 = Player(x * TILE_SIZE, y * TILE_SIZE, "keyboard", "images/player 1.png")  # Player 1 (keyboard)
        elif tile == "M":
            player2 = Player(x * TILE_SIZE, y * TILE_SIZE, "mouse", "images/player 2.png")  # Player 2 (mouse)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Draw the background
    screen.blit(background, (0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update players
    player1.handle_input()
    player1.update()
    player2.handle_input()
    player2.update()

    # Draw platform blocks (now just rectangles)
    for block in blocks:
        pygame.draw.rect(screen, BLACK, block)  # Draw a black rectangle for each block

    # Draw the players
    screen.blit(player1.image, (player1.rect.x, player1.rect.y))
    screen.blit(player2.image, (player2.rect.x, player2.rect.y))

    pygame.display.flip()
    clock.tick(60)  # Increased to 60 FPS for smoother gameplay

pygame.quit()
