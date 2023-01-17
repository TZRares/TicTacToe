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
#------------------Define First Player-----------------------
    def get_random_first_player(game):
        return random.randint(0, 1)
#------------------Define Player Spot------------------------
    def fix_spot(game, row, col, player):
        game.board[row][col] = player
#------------------Define Win/Tie Logic---------------------
    def is_player_win(game, player):
        win = None

        n = len(game.board)
#----------------Rows Check-----------------------------
        for i in range(n):
            win = True
            for j in range(n):
                if game.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
#----------------Column Check----------------------------
        for i in range(n):
            win = True
            for j in range(n):
                if game.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
#----------------Diagonal Check---------------------------
        win = True
        for i in range(n):
            if game.board[i][i] != player:
                win = False
                break
        if win:
            return win
#-----------------Win true---------------------------------
        win = True
        for i in range(n):
            if game.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in game.board:
            for item in row:
                if item == '-':
                    return False
        return True
#------------------Define Board Fill------------------------
    def is_board_filled(game):
            for row in game.board:
                for item in row:
                    if item == '-':
                        return False
            return True
#------------------Player Swap-----------------------------
    def swap_player_turn(game, player):
        return 'X' if player == 'O' else 'O'
#------------------Board Generation--------------------------
    def show_board(game):
        for row in game.board:
            for item in row:
                print(item, end=" ")
            print()
#------------------Board Logic-----------------------------
    def start(game):
        game.board_create()
#-----------------Start Game----------------------------
        player = 'X' if game.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")
#-----------------Board Showing----------------------------
            game.show_board()
#-----------------User Input----------------------------
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()
#-----------------Spot Fixing----------------------------
            game.fix_spot(row - 1, col - 1, player)
#-----------------Win Status----------------------------
            if game.is_player_win(player):
                print(f"Player {player} Won!")
                break
#-----------------Game Status----------------------------
            if game.is_board_filled():
                print("Match Draw!")
                break
#-----------------Turn Swap----------------------------
            player = game.swap_player_turn(player)
#-----------------Final Board Update----------------------------
        print()
        game.show_board()
#-----------------Start Game----------------------------

tic_tac_toe = TicTacToe()
tic_tac_toe.start()