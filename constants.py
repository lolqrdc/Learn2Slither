from enum import Enum

BOARD_SIZE = 10
INIT_SNAKE_LENGTH = 3
NUM_GREEN_APPLES = 2
NUM_RED_APPLES = 1


class Action(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Event(Enum):
    GREEN = "green"
    RED = "red"
    DEAD = "dead"
    NONE = "none"


REWARD_GREEN_APPLE = 10
REWARD_RED_APPLE = -10
REWARD_STEP = -1
REWARD_DEAD = -100

# Q-learning hyperparameters
ALPHA = 0.1
GAMMA = 0.99
EPSILON = 1.0
EPSILON_MIN = 0.01
EPSILON_DECAY = 0.995

# Display constants
CELL_SIZE = 60
FPS_FAST = 60
FPS_NORMAL = 10
FPS_SLOW = 3

# Colors
COLOR_BG = (30, 30, 30)
COLOR_GRID = (50, 50, 50)
COLOR_SNAKE_HEAD = (100, 149, 237)
COLOR_SNAKE_BODY = (65, 105, 225)
COLOR_GREEN_APPLE = (50, 255, 50)
COLOR_RED_APPLE = (220, 20, 60)

