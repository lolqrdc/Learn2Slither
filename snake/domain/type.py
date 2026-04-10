""" Types du domaine (Direction, Pos). """

from enum import Enum 

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @property
        def dx(self) -> int:
            return (self.value[0])
    
    @property
        def dy(self) -> int:
            return (self.value[1])

@dataclass(frozen=True, slots=True)
class Position:
    x: int
    y: int

    def move(self, direction: Direction) -> "Position":
        return (Pos(self.x + direction.dx, self.y + direction.dy))
