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
        self.state = 'start'

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            if self.state == 'playing':
                pass

            # update the clock
            self.clock.tick(FPS)

        # uninitialize all pygame modules
        pygame.quit()
        # exit from Python
        sys.exit()

    ########## HELPER FUNCTIONS ##########
    def draw_text(self, words, screen, position, size, color, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        # get the dimensions (width, height)
        text_size = text.get_size()
        if centered:
            position[0] = position[0] - text_size[0] // 2
            position[1] = position[1] - text_size[1] // 2
        screen.blit(text, position)

    ########## INTRO FUNCTIONS ##########
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('HIGH SCORE', self.screen, [4, 0], START_FONT_SIZE, (255, 255, 255), START_FONT)
        self.draw_text('PRESS SPACEBAR TO PLAY', self.screen, [WIDTH // 2, HEIGHT // 2], START_FONT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.draw_text('1 PLAYER ONLY', self.screen, [WIDTH // 2, HEIGHT // 2 + 50], START_FONT_SIZE, (44, 167, 198), START_FONT, centered=True)
        pygame.display.update()