import pygame

# Initialize pygame package
pygame.init()

# Create a screen of 800(W) x 600(H)
screen = pygame.display.set_mode((800, 600))

# Title & Icon
pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("img/ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("img/spaceship.png")

playerX = 370
playerY = 480


def player(x, y):
    # blit = draw an image on the screen
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        # close button = quit event
        if event.type == pygame.QUIT:
            running = False

    # Background
    screen.fill((0, 0, 0))

    playerX += 1
    # playerX -= 1
    # playerY += 1
    # playerY -= 1
    player(playerX, playerY)

    # Screen needs to update within the loop
    pygame.display.update()