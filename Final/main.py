import random
from game import constants
from game.director import director
from game.actor import actor
from game.point import point
from game.input_service import inputservice
from game.output_service import outputservice


def main():
    cast = {}

    input_service = inputservice()
    output_service = outputservice()


    output_service.open_window()