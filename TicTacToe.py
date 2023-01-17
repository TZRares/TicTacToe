import random

class TicTacToe:

    def __init__(game):
        game.board = []

    def board_create(game):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            game.board.append(row)

    def show_board(game):
        for row in game.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(game):
        game.board_create()
        
        game.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()