import pygame

# Initialize pygame package
pygame.init()

# Create a screen of 800(H) x 600(W)
screen = pygame.display.set_mode((800, 600))

# Title & Icon
pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("img/spacecraft.png")
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        # close button = quit event
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.update()