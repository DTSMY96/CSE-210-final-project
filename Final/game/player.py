from game.actor import Actor
from game.point import Point
from game import constants

class player(Actor):
    def __init__(self):
        super().__init__()
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._width = ""
        self._height = ""

        
