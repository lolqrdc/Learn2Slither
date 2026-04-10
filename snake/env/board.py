""" Implémentation du board de jeu suivant les constantes du sujet. """

import random
from snake.domain import Direction, Position

class BoardEnv:
    """ Constantes imposées par le sujet """
    WIDTH = 10
    HEIGHT = 10

    INITIAL_SNAKE_LEN = 3
    GREEN_APPLE_COUNT = 2
    RED_APPLE_COUNT = 1

    # -- constructeur -- 
    def __init__(self, seed: int | None = None) -> None:
        self.random = random.Random(seed)

        self.snake: list[Position]
        self.green_apples: set[Position]
        self.red_apple: Position

        self.reset()
