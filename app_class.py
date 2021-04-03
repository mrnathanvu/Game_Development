import pygame, sys
from settings import *

from player_class import *

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

        # 560 / 28 = 20
        self.cell_width = MAZE_WIDTH // 28
        # 620 / 30 = 20.7
        self.cell_height = MAZE_HEIGHT // 30

        self.walls = []
        self.coins = []
        self.p_pos = None

        self.load()

        self.player = Player(self, self.p_pos)

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False

            # update the clock
            self.clock.tick(FPS)

        # uninitialize all pygame modules
        pygame.quit()
        # exit from Python
        sys.exit()

    #################### HELPER FUNCTIONS ####################
    def draw_text(self, words, screen, position, size, color, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        # get the dimensions (width, height)
        text_size = text.get_size()
        if centered:
            position[0] = position[0] - text_size[0] // 2
            position[1] = position[1] - text_size[1] // 2
        screen.blit(text, position)

    def load(self):
        self.background = pygame.image.load('img/background.png')
        # resize to new resolution
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))

        # Opening walls file
        # Creating walls list with co-ords of wall
        with open('walls.txt', 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx))
                    elif char == "P":
                        self.p_pos = vec(xidx, yidx)
        # print(self.walls)
        # print(len(self.walls))

    def draw_grid(self):
        # 560 / 20 = 28 lines
        for x in range(WIDTH // self.cell_width):
            # draw vertical lines (start position of the line -> end position of the line, (x, y)
            pygame.draw.line(self.background, (107, 107, 107), (x * self.cell_width, 0), (x * self.cell_width, HEIGHT))

        # 620 / 20.7 = 30 lines
        for x in range(HEIGHT // self.cell_height):
            # draw horizontal lines (start position of the line -> end position of the line, (x, y)
            pygame.draw.line(self.background, (107, 107, 107), (0, x * self.cell_height), (WIDTH, x * self.cell_height))

        # for wall in self.walls:
        #     pygame.draw.rect(self.background, (107, 107, 107),
        #                     (wall.x * self.cell_width, wall.y * self.cell_height,
        #                      self.cell_width, self.cell_height))
        # for coin in self.coins:
        #     pygame.draw.rect(self.background, (255, 255, 0),
        #                     (coin.x * self.cell_width, coin.y * self.cell_height,
        #                      self.cell_width, self.cell_height))

    #################### INTRO FUNCTIONS ####################
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
        self.draw_text('HIGH SCORE: 0', self.screen, [4, 0], START_FONT_SIZE, (255, 255, 255), START_FONT)
        self.draw_text('PRESS SPACEBAR TO PLAY', self.screen, [WIDTH // 2, HEIGHT // 2], START_FONT_SIZE,
                       (170, 132, 58), START_FONT, centered=True)
        self.draw_text('1 PLAYER ONLY', self.screen, [WIDTH // 2, HEIGHT // 2 + 50], START_FONT_SIZE, (44, 167, 198),
                       START_FONT, centered=True)
        pygame.display.update()

    #################### PLAYING FUNCTIONS ####################
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))

    def playing_update(self):
        self.player.update()

    def playing_draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER // 2, TOP_BOTTOM_BUFFER // 2))
        self.draw_coins()
        # self.draw_grid()
        self.draw_text('HIGH SCORE: {}'.format(self.player.current_score), self.screen, [4, 0], START_FONT_SIZE, (255, 255, 255), START_FONT)
        self.draw_text('CURRENT SCORE: 0', self.screen, [254, 0], START_FONT_SIZE, (255, 255, 255), START_FONT)
        self.player.draw()
        pygame.display.update()
        # self.coins.pop()

    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(self.screen, (254, 226, 62),
                              (int(coin.x * self.cell_width) + self.cell_width // 2 + TOP_BOTTOM_BUFFER // 2,
                               int(coin.y * self.cell_height) + self.cell_height // 2 + TOP_BOTTOM_BUFFER // 2), 5)
