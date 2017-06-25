'''
  * Python Programming for Data Scientists and Engineers
  * LAB #3-3 Tic Tac Toe Game
  * #11 Chia-Hui Amy Lin
'''

# 1. Create a function to ask for coordinates from each player 1 turn by turn.
# Coordinate = (row, col) --> User entered
# 2. Check the input coordinate is occupied or not.
# If yes, prompt user for coordinate again
# 3. If cells are all occupied, end the game.


def draw_board(board_array):
    for row in range(len(board_array)):
        print('-'*((len(board_array[0]))*2 + 1))
        print('|', end='')
        for column in range(len(board_array[row])):
            print(board_array[row][column], end='|')
        print(' ')
    print('-'*((len(board_array[0]))*2 + 1))
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


def player_one(player_move_board):
    flag = False
    while True:
        try:
            print("< Player 1's Turn >")
            player_move_row, player_move_col = map(int, input("Please make your move with numbers of (row, column) :").split(","))
            # player_move_row, player_move_col = int(player_move_row, player_move_col)
        except ValueError or TypeError or IndexError:
            print("Invalid input. Please enter an INTEGER." + "\n")
            flag = True
        else:
            break
    if player_move_board[player_move_row][player_move_col] == " ":
        player_move_board[player_move_row][player_move_col] = "X"
    else:
        print("Oops, spot is taken. Please enter another one!" + "\n")
        flag = True
        return False
    return player_move_board


def player_two(player_move_board):
    flag = False
    while True:
        try:
            print("< Player 2's Turn >")
            player_move_row, player_move_col = map(int, input("Please make your move with numbers of (row, column) :").split(","))
            # player_move_row, player_move_col = int(player_move_row, player_move_col)
        except ValueError or TypeError or IndexError:
            print("Invalid input. Please enter an INTEGER." + "\n")
            flag = True
        else:
            break
    if player_move_board[player_move_row][player_move_col] == " ":
        player_move_board[player_move_row][player_move_col] = "O"
    else:
        print("Oops, spot is taken. Please enter another one!" + "\n")
        flag = True
        return False
    return player_move_board


def board_full(current_board):
    full = True
    for check_row in range(len(current_board)):
        for check_column in range(len(current_board[check_row])):
            if current_board[check_row][check_column] == " ":
                full = False
    return full


# -------------------------------------------------- Main --------------------------------------------------
blank_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print("[  Welcome to Tic Tac Toe Game! Ready to have some battles? ;) ]")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
player_one_prompt = False
while True:
    update_board = player_one(blank_board)
    if update_board:
        draw_board(update_board)
        check_full = board_full(update_board)
        if check_full:
            print("End of Game!")
            break

        update_board = player_two(update_board)
        if update_board:
            draw_board(update_board)
            check_full = board_full(update_board)
            if check_full:
                print("xxxxxxxxxxxxxxxx End of Game! xxxxxxxxxxxxxxxx")
                break

