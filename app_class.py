import pygame, sys
from settings import *

pygame.init()
# a 2-Dimensional Vector
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # compute the clock framerate (FPS) / create an object to help track time
        self.clock = pygame.time.Clock()

        self.running = True
        self.state = 'intro'

    def run(self):
        while self.running:
            if self.state == 'intro':
                self.intro_events()
                self.intro_update()
                self.intro_draw()
            else:
                pass

            # update the clock
            self.clock.tick(FPS)

        # uninitialize all pygame modules
        pygame.quit()
        # exit from Python
        sys.exit()

    ##### INTRO FUNCTIONS #####

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def intro_update(self):
        pass

    def intro_draw(self):
        pygame.display.update()