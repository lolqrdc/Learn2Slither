""" Sous-package environnement : board, règles, évolution de la partie. """

from .board import BoardEnv, UP, LEFT, DOWN, RIGHT

__all__ = ["BoardEnv", "UP", "DOWN", "LEFT", "RIGHT"]
