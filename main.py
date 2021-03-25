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
playerX_change = 0


def player(x, y):
    # blit = draw an image on the screen
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:
    # Background
    screen.fill((0, 0, 0))

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

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    # spaceship.png is 64x64, so 800-64=736
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)

    # Screen needs to update within the loop
    pygame.display.update()