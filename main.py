import pygame
import random

# Initialize pygame package
pygame.init()

# Create a screen of 800(W) x 600(H)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("img/background.jpg")

# Title & Icon
pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("img/ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("img/spaceship.png")

playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("img/alien.png")

enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 40


def player(x, y):
    # blit = draw an image on the screen
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game loop
running = True
while running:
    # Background color
    screen.fill((0, 0, 0))
    # Background image, draw the image from the top left conner
    screen.blit(background, (0, 0))

    # Events
    for event in pygame.event.get():
        # close button = quit event
        if event.type == pygame.QUIT:
            running = False

        # Keystroke events
        # if an keystrokes is pressed
        if event.type == pygame.KEYDOWN:
            # if the keystroke being pressed is the left key
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            # if the keystroke being pressed is the right key
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        # if an keystrokes is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # The spaceship stops when a keystroke is released
                playerX_change = 0

    # Movement boundaries  for player
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    # spaceship.png is 64x64, so 800-64=736
    elif playerX >= 736:
        playerX = 736

    # Movement boundaries for enemy
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    # Screen needs to update within the loop
    pygame.display.update()