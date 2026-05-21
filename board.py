import random
from collections import deque
from constants import (
    BOARD_SIZE,
    INIT_SNAKE_LENGTH,
    NUM_GREEN_APPLES,
    NUM_RED_APPLES,
    Action,
    Event
)


class Board:
    """Represents the game environment."""

    def __init__(self):
        """Initialize empty board state."""
        self.size = BOARD_SIZE
        self.snake = deque()
        self.direction = None
        self.green_apples = []
        self.red_apples = []
        self.game_over = False

    def reset(self):
        """Reset board to a fresh random state."""
        self.snake = deque()
        self.green_apples = []
        self.red_apples = []
        self.game_over = False
        self.direction = random.choice(
            [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]
        )
        self._place_snake()
        for _ in range(NUM_GREEN_APPLES):
            self._place_apple_at_random(is_green=True)
        for _ in range(NUM_RED_APPLES):
            self._place_apple_at_random(is_green=False)

    def step(self, action):
        """Apply action, update state, return Event."""
        if action in [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]:
            self.direction = action

            head_row, head_col = self.snake[0]
            if self.direction == Action.UP:
                head_row -= 1
            elif self.direction == Action.DOWN:
                head_row += 1
            elif self.direction == Action.LEFT:
                head_col -= 1
            elif self.direction == Action.RIGHT:
                head_col += 1

            if (not self._is_within_bounds(head_row, head_col) or
                    (head_row, head_col) in self.snake):
                self.game_over = True
                return Event.DEAD

            self.snake.appendleft((head_row, head_col))

            if (head_row, head_col) in self.green_apples:
                self.green_apples.remove((head_row, head_col))
                self._place_apple_at_random(is_green=True)
                return Event.GREEN

            elif (head_row, head_col) in self.red_apples:
                self.red_apples.remove((head_row, head_col))
                self._place_apple_at_random(is_green=False)
                self.snake.pop()
                self.snake.pop()
                if len(self.snake) == 0:
                    self.game_over = True
                    return Event.DEAD
                return Event.RED
            else:
                self.snake.pop()
                return Event.NONE

    def is_game_over(self):
        """Return True if the game has ended."""
        return self.game_over

    def get_grid(self):
        """Return the 2D grid for the interpreter."""
        grid = [[None for _ in range(self.size)]
                for _ in range(self.size)]
        for i, (row, col) in enumerate(self.snake):
            grid[row][col] = "H" if i == 0 else "S"
        for row, col in self.green_apples:
            grid[row][col] = "G"
        for row, col in self.red_apples:
            grid[row][col] = "R"
        return grid

    def snake_length(self):
        """Return current snake length."""
        return len(self.snake)

    def _is_within_bounds(self, row, col):
        """Return True if position is inside the grid."""
        return 0 <= row < self.size and 0 <= col < self.size

    def _get_empty_cells(self):
        """Return list of all empty cell positions."""
        occupied = set(self.snake) | set(self.green_apples) | set(
            self.red_apples
        )
        return [
            (row, col)
            for row in range(self.size)
            for col in range(self.size)
            if (row, col) not in occupied
        ]

    def _place_apple_at_random(self, is_green=True):
        """Find a random empty cell and return its position."""
        empty_cells = self._get_empty_cells()
        if empty_cells:
            pos = random.choice(empty_cells)
            if is_green:
                self.green_apples.append(pos)
            else:
                self.red_apples.append(pos)
            return pos

    def _place_snake(self):
        """Place snake randomly with initial length."""
        opposite = {
            Action.UP: (1, 0),
            Action.DOWN: (-1, 0),
            Action.LEFT: (0, 1),
            Action.RIGHT: (0, -1)
        }
        while True:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            dr, dc = opposite[self.direction]
            segments = [
                (row + i * dr, col + i * dc) for i in range(INIT_SNAKE_LENGTH)
            ]
            if all(self._is_within_bounds(r, c)
                   for r, c in segments):
                self.snake = deque(segments)
                break
