import logging
import sys
import random

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='SnakeAndLadder : %(message)s')

class SnakeAndLadder:

    def __init__(self, board_size: int=100, config: dict={}, dieOptions=[1, 2, 3, 4, 5, 6]) -> None:
        self.board_size = board_size
        self.config = config
        self.validateConfig()
        self.dieOptions = dieOptions
        self.log("Initializing snake and ladder in a board of size of {}".format(board_size))

    def validateConfig(self):
        for key, value in self.config.items():
            if not 0 < value + key <= self.board_size:
                logging.error("InvalidConfiguration : {} steps at position {}".format(value, key))
                logging.error("Exiting game")
                sys.exit()

    def play(self, turns):
        self.log("Starting game with {} turns at position 1".format(turns))
        position = 1
        while turns > 0:
            diceRoll = self.getDiceRoll()
            
            if position == self.board_size:
                self.log("Player has won with {} turns left".format(turns))
                sys.exit()
            else:
                jumpPosition = position + diceRoll
                if jumpPosition in self.config:
                    position = self.config[jumpPosition] + jumpPosition
                    if self.config[jumpPosition] > 0:
                        self.log("Die rolled {} and player moved to position {}".format(diceRoll, jumpPosition))
                        self.log("Yay a ladder! Jumping {} steps ahead to position {}".format(self.config[jumpPosition], position))
                    else:
                        self.log("Die rolled {} and player moved to position {}".format(diceRoll, jumpPosition))
                        self.log("Uh-oh a snake! Jumping back {} steps to position {}".format(abs(self.config[jumpPosition]), position))
                elif position + diceRoll > 100:
                    self.log("Player cannot move ahead with die roll {} from position {}".format(diceRoll, position))
                else:
                    position = jumpPosition
                    self.log("Die rolled {} and player moved to position {}".format(diceRoll, position))
            turns -= 1

        self.log("Uh-oh! Player lose :(")

    def getDiceRoll(self):
        return random.choice(self.dieOptions)

    def log(self, message: str) -> None:
        logging.info(message)