class Interpreter:
    """Converts board state into snake vision."""

    def get_state(self, board):
        """Return snake vision as a tuple of 4 direction tuples."""
        grid = board.get_grid()
        head_row, head_col = board.snake[0]
        up = self._look(grid, head_row, head_col, -1, 0)
        down = self._look(grid, head_row, head_col, 1, 0)
        left = self._look(grid, head_row, head_col, 0, -1)
        right = self._look(grid, head_row, head_col, 0, 1)
        return (up, down, left, right)

    def _look(self, grid, row, col, dr, dc):
        """Return what the snake sees in one direction as a tuple."""
        vision = []
        row += dr
        col += dc
        while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            cell = grid[row][col]
            if cell is None:
                cell = "0"
            vision.append(cell)
            row += dr
            col += dc
        vision.append("W")
        return tuple(vision)
