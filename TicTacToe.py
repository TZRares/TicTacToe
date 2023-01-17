import random

class TicTacToe:
#------------------Game initialization------------------------
    def __init__(game):
        game.board = []
#------------------Board design-------------------------------
    def board_create(game):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            game.board.append(row)
#------------------Board Generation--------------------------
    def show_board(game):
        for row in game.board:
            for item in row:
                print(item, end=" ")
            print()
#------------------Define First Player-----------------------
    def get_random_first_player(game):
        return random.randint(0, 1)
#------------------Define Player Spot------------------------
    def fix_spot(game, row, col, player):
        game.board[row][col] = player
#------------------Define Board Check------------------------
    def is_board_filled(game):
            for row in game.board:
                for item in row:
                    if item == '-':
                        return False
            return True

#------------------Board Logic-----------------------------
    def start(game):
        game.board_create()
#------------------Player's Turn---------------------------
        player = 'X' if game.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")
#------------------Show Board------------------------------
            game.show_board()
#------------------Recieve Player Input--------------------
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()
#---------------------Start Game-----------------------------
tic_tac_toe = TicTacToe()
tic_tac_toe.start()