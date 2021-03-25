from pygame.math import Vector2 as vec

# Screen settings
WIDTH, HEIGHT = 610, 670  # 560 + 50 and 620 + 50 from TOP_BOTTOM_BUFFER
FPS = 60
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH - TOP_BOTTOM_BUFFER, HEIGHT - TOP_BOTTOM_BUFFER

# Color settings
BLACK = (0, 0, 0)

# Font settings
START_FONT_SIZE = 16
START_FONT = 'arial black'
# Player settings
PLAYER_START_POS = vec(1, 1)
PLAYER_COLOR = (190, 194, 15)
# Mob settings
