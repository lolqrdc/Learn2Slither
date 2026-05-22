import pygame
import sys
from constants import (
    BOARD_SIZE,
    CELL_SIZE,
    FPS_NORMAL,
    COLOR_BACKGROUND,
    COLOR_GRID,
    COLOR_SNAKE_HEAD,
    COLOR_SNAKE_BODY,
    COLOR_GREEN_APPLE,
    COLOR_RED_APPLE
)

WINDOW_SIZE = BOARD_SIZE * CELL_SIZE

class Display:
    """Handles pygame graphical rendering."""

    def __init__(self, fps=FPS_NORMAL, step_b_step=False):
        """ Init pygame window."""
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Learn2Slither")
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.step_b_step = step_b_step
    
    def render(self, board):
        """Draw the current board state."""
        self.screen.fill(COLOR_BACKGROUND)

        # Draw grid
        for x in range(0, WINDOW_SIZE, CELL_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (x, 0), (x, WINDOW_SIZE))
        for y in range(0, WINDOW_SIZE, CELL_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (0, y), (WINDOW_SIZE, y))

        # Draw snake
        for i, (row, col) in enumerate(board.snake):
            color = COLOR_SNAKE_HEAD if i == 0 else COLOR_SNAKE_BODY
            self._draw_cell(row, col, color)

        # Draw green apples
        for row, col in board.green_apples:
            self._draw_cell(row, col, COLOR_GREEN_APPLE)

        # Draw red apples
        for row, col in board.red_apples:
            self._draw_cell(row, col, COLOR_RED_APPLE)

        pygame.display.flip()
        self.clock.tick(self.fps)

    def wait_for_keypress(self):
        """Wait for user to press a key."""
        pass

    def close(self, board):
        """ Close the pygame window."""
        pass

    def _draw_cell(self, row, col, color):
        """ Draw single cell colored at given pos. """
        x = col * CELL_SIZE
        y = row * CELL_SIZE
        pygame.draw.rect(
            self.screen, color,
            (x, y, CELL_SIZE, CELL_SIZE)
        )

    def _handle_events(self):
        """ Handle pygame events return false if quit. """
        pass

