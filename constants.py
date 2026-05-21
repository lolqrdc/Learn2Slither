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
