from game.actor import actor
from game.point import point
from game import constants

class player(actor):
    def __init__(self):
        super().__init__()
        self._position = point(0, 0)
        self._velocity = point(0, 0)
        self._width = ""
        self._height = ""

        
