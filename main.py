import pygame
import random
import math

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
enemyImg = []

enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("img/alien.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load("img/bullet.png")

bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

# Scoreboard
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10


def player(x, y):
    # blit = draw an image on the screen
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"

    screen.blit(bulletImg, (x + 16, y + 10))


# Distance between two points and the midpoint
# D=sqrt((x2−x1)^2+(y2−y1)^2)
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

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
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Get the spaceship current x coordinate
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
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
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    show_score(textX, textY)

    # Screen needs to update within the loop
    pygame.display.update()
