
from snake_and_ladder import SnakeAndLadder

def test():
    # key = position at which snake/ladder starts
    # value = number of places ahead/back it takes indicated by +ve/-ve numbers
    config = { 10 : 5, 17 : 9, 28 : 11, 33 : -8, 40 : 3, 51 : -10, 62 : 9, 73 : -15, 82: 6,  95: -20 }
    game = SnakeAndLadder(config=config)
    game.play(20)


if __name__ == "__main__":
    test()