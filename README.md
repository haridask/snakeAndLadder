# snakeAndLadder
Snake and Ladder single player game

Initialization options

config: dict<int, int>

    key: position at which snakes/ladders appear
    value: number of steps to jump ahead/back
    default: {}

dieOptions: Array

    supported dieOptions
    default: [1, 2, 3, 4, 5, 6]

To run:

    from snake_and_ladder import SnakeAndLadder

    snakeAndLadder = SnakeAndLadder(config, dieOptions)
    snakeAndLadder.play()