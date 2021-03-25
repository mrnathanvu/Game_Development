import pygame

pygame.init()

# Create a screen of 800(H) x 600(W)
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        # close button = quit event
        if event.type == pygame.QUIT:
            running = False