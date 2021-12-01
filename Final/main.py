import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.input_service import inputservice
from game.output_service import outputservice


def main():
    cast = {}

    input_service = inputservice()
    output_service = outputservice()


    output_service.open_window()


    director = Director(cast, script)
    director.start_game()