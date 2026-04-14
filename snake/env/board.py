""" Implémentation du board de jeu suivant les constantes du sujet. """

import random
from snake.domain import Direction, Position

class BoardEnv:
    """ Constants imposed by the subject. """
    WIDTH = 10
    HEIGHT = 10

    INITIAL_SNAKE_LEN = 3
    GREEN_APPLE_COUNT = 2
    RED_APPLE_COUNT = 1

    # -- constructor method -- 
    def __init__(self, seed: int | None = None) -> None:
        self.random = random.Random(seed)

        self.snake: list[Position]
        self.green_apples: set[Position]
        self.red_apple: Position

        self.reset()

    def reset(self) -> None:
        """ Reset the state of the board. """
        self._spawn_snake()
        self._spawn_apples()
    
    def _spawn_snake(self) -> None:
        """Place the initial snake on the board."""
        direction = self.random.choice(list(Direction))
        
        head_x = self.random.randint(0, self.WIDTH - 1)
        head_y = self.random.randint(0, self.HEIGHT - 1)
        head = Position(head_x, head_y)

        self.snake = [head]

        curr = head
        for _ in range(self.INITIAL_SNAKE_LEN - 1): 
            next_pos = Position(
                curr.x - direction.dx,
                curr.y - direction.dy,
            )
            if not self._is_inside(next_pos):
                self._spawn_snake()
                return
            
            self.snake.append(next_pos)
            curr = next_pos
    
    def _spawn_apples(self) -> None:
        """Placeholder for apple spawning."""
        occupied = set(self.snake)

        free_pos:list[Position] = []
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                pos = Position(x, y)
                if pos not in occupied:
                    free_pos.append(pos)
        
        if len(free_pos) < self.GREEN_APPLE_COUNT + self.RED_APPLE_COUNT:
            raise RuntimeError("Not enough free positions to place apples.")
        
        self.green_apples = set(
            self.random.sample(free_pos, self.GREEN_APPLE_COUNT)
        )
        
        remaining_pos = [
            pos for pos in free_pos if pos not in self.green_apples
        ]
        self.red_apple= self.random.choice(remaining_pos)


    def _is_inside(self, pos: Position) -> bool:
        return (
            0 <= pos.x < self.WIDTH and 
            0 <= pos.y < self.HEIGHT
        )
