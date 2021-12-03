import logging
from os import name
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='SnakeAndLadder : %(message)s')

class SnakeAndLadder:

    def __init__(self, board_size: int=100) -> None:
        self.board_size = board_size
        self.log("Initializing snake and ladder in a board of size of {}".format(board_size))

    def play(self, turns):
        self.log("Starting game with {} turns".format(turns))
        pass

    def getDiceRoll(self):
        pass

    def log(self, message: str) -> None:
        logging.info(message)