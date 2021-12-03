
from snake_and_ladder import SnakeAndLadder

def test():
    config = { 10 : 5, 17 : 9, 28 : 11, 33 : -8, 40 : 3, 51 : -10, 62 : 9, 73 : -15, 82: 6,  95: -20 }
    game = SnakeAndLadder(config=config)
    game.play(20)

def testStory2():
    config = {14 : -7}
    game = SnakeAndLadder(config=config)
    game.play(20)

def testStory3():
    game = SnakeAndLadder(dieOptions=[2, 4, 6])
    assert game.dieOptions == [2, 4, 6]
    game.play(20)

def testDieOptionsAssignment():
    game = SnakeAndLadder(dieOptions=[1])
    assert game.dieOptions == [1]

def testConfigAssignment():
    game = SnakeAndLadder(config={10: 5})
    assert game.config == {10 : 5}

def testBoardSizeAssignment():
    game = SnakeAndLadder(board_size=50)
    assert game.board_size == 50
    game.play(20)

if __name__ == "__main__":
    test()
    testDieOptionsAssignment()
    testConfigAssignment()
    testBoardSizeAssignment()
    testStory2()
    testStory3()
