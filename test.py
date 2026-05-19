import unittest
from board import Board
from interpreter import Interpreter
from constants import Action, Event
from collections import deque


class TestBoard(unittest.TestCase):
    """Test Board class functionality."""

    def setUp(self):
        self.board = Board()
        self.board.reset()

    def test_board_initialization(self):
        """Test board initializes with correct state."""
        self.assertEqual(self.board.size, 10)
        self.assertEqual(len(self.board.snake), 3)
        self.assertEqual(len(self.board.green_apples), 2)
        self.assertEqual(len(self.board.red_apples), 1)
        self.assertFalse(self.board.game_over)

    def test_snake_movement(self):
        """Test snake moves in correct direction."""
        # serpent connu : tête en (5,5), corps en-dessous
        self.board.snake = deque([(5, 5), (6, 5), (7, 5)])
        self.board.direction = Action.UP
        initial_head = self.board.snake[0]
        self.board.step(Action.UP)
        new_head = self.board.snake[0]
        self.assertEqual(new_head[0], initial_head[0] - 1)

    def test_green_apple_collision(self):
        """Test eating green apple increases length."""
        # serpent connu : corps en-dessous, case au-dessus libre
        self.board.snake = deque([(5, 5), (6, 5), (7, 5)])
        self.board.direction = Action.UP
        initial_length = len(self.board.snake)
        self.board.green_apples = [(4, 5)]   # juste au-dessus, libre
        self.board.red_apples = [(9, 9)]     # loin
        event = self.board.step(Action.UP)
        self.assertEqual(event, Event.GREEN)
        self.assertEqual(len(self.board.snake), initial_length + 1)

    def test_red_apple_collision(self):
        """Test eating red apple decreases length by 1."""
        initial_length = len(self.board.snake)
        # Place apple at the position the head will move to
        head_row, head_col = self.board.snake[0]
        self.board.red_apples = [(head_row - 1, head_col)]
        self.board.direction = Action.UP
        event = self.board.step(Action.UP)
        self.assertEqual(event, Event.RED)
        self.assertEqual(len(self.board.snake), initial_length - 1)

    def test_wall_collision(self):
        """Test collision with wall ends game."""
        self.board.snake = [(0, 0), (0, 1), (0, 2)]
        self.board.direction = Action.UP
        event = self.board.step(Action.UP)
        self.assertEqual(event, Event.DEAD)
        self.assertTrue(self.board.game_over)

    def test_self_collision(self):
        """Test collision with self ends game."""
        self.board.snake = [(5, 5), (5, 4), (5, 3), (5, 4)]
        event = self.board.step(Action.LEFT)
        self.assertEqual(event, Event.DEAD)
        self.assertTrue(self.board.game_over)


class TestInterpreter(unittest.TestCase):
    """Test Interpreter class functionality."""

    def setUp(self):
        self.board = Board()
        self.board.reset()
        self.interpreter = Interpreter()

    def test_get_state_returns_tuple(self):
        """Test get_state returns 4-tuple."""
        state = self.interpreter.get_state(self.board)
        self.assertEqual(len(state), 4)
        for direction in state:
            self.assertIsInstance(direction, tuple)

    def test_vision_contains_wall(self):
        """Test vision always ends with wall marker."""
        state = self.interpreter.get_state(self.board)
        for direction in state:
            self.assertEqual(direction[-1], "W")

    def test_vision_identifies_snake(self):
        """Test vision identifies snake segments."""
        self.board.snake = [(5, 5), (5, 4), (5, 3)]
        state = self.interpreter.get_state(self.board)
        all_vision = "".join("".join(str(v) for v in d) for d in state)
        self.assertIn("S", all_vision)

    def test_vision_identifies_apples(self):
        """Test vision identifies apple types."""
        head_row, head_col = self.board.snake[0]
        # Place green apple directly above
        self.board.green_apples = [(head_row - 1, head_col)]
        # Place red apple directly below
        self.board.red_apples = [(head_row + 1, head_col)]
        state = self.interpreter.get_state(self.board)
        all_vision = "".join("".join(v for v in d) for d in state)
        self.assertIn("G", all_vision)
        self.assertIn("R", all_vision)


if __name__ == "__main__":
    unittest.main()
