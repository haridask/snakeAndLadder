# Snake And Ladder
Snake and Ladder single player game

Options

config: dict<int, int> <i>Optional</i>

    key: position at which snakes/ladders appear
    value: number of steps to jump ahead/back
    default: {}

dieOptions: Array <i>Optional </i>

    supported dieOptions
    default: [1, 2, 3, 4, 5, 6]

turns: int <i> Required </i>

    Number of turns to play


To run:

    from snake_and_ladder import SnakeAndLadder

    snakeAndLadder = SnakeAndLadder(config, dieOptions)
    snakeAndLadder.play(20)