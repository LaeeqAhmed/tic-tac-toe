#global variables
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
is_valid=True
winner=None
print("SELECT EITHER 'X' OR 'O' ")
current_palyer=input()
if current_palyer=="X":
    current_palyer="X"
else: current_palyer="O"
#functions
def display_board():
    print(board[0] + " | ", board[1] + " | ", board[2]+ "     1 | 2 | 3")
    print(board[3] + " | ", board[4] + " | ", board[5]+ "     4 | 5 | 6")
    print(board[6] + " | ", board[7] + " | ", board[8]+ "     7 | 8 | 9")
def play_game():
    display_board()#first of all display board
    while is_valid:
        whoose_turn(current_palyer)
        #check if game over
        game_over()
        flip_player()
    if winner=="X":
        print(winner+ " WON BETTER LUCK NEXT TIME 'O' ")
    elif winner=="O":
        print(winner+ " WON BETTER LUCK NEXT TIME 'X' ")
    elif winner == None:
        print("IT'S TIE")



#handle a turn
def whoose_turn(player):
    print(player+"'s turn")
    print("input from the position 1-9")
    position=int(input())
    while not True:
        print("input from position 1-9")
    position=int(position)-1
    board[position]=player
    display_board()
#flip the player from current to next state
def flip_player():
    global current_palyer

    if current_palyer=="X":
        current_palyer="O"
    elif current_palyer=="O":
        current_palyer="X"

def game_over():
    '''check for winner'''
    check_for_winner()
    #check for tie
    check_tie()

def check_for_winner():
    global winner
    row_winner=check_rows()
    col_winner=check_col()
    diagonal_winner=check_diagonal()
    if row_winner:
        winner=row_winner
    elif col_winner:
        winner=col_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None



def check_rows():
    global is_valid
    row1 = board[0]==board[1]==board[2] != "-"
    row2 = board[3]==board[4]==board[5] != "-"
    row3 = board[6]==board[7]==board[8] != "-"
    if row1 or row2 or row3:
        is_valid=False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else: return None

def check_col():
    global is_valid
    col1 = board[0]==board[3]==board[6] != "-"
    col2 = board[1]==board[4]==board[7] != "-"
    col3 = board[2]==board[5]==board[8] != "-"
    if col1 or col2 or col3:
        is_valid=False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    else: return None

def check_diagonal():
    global is_valid
    dig1 = board[0]==board[4]==board[8] != "-"
    dig2 = board[2]==board[4]==board[6] != "-"
    if dig1 or dig2:
        is_valid=False
    if dig1:
        return board[0]
    elif dig2:
        return board[2]
    else: return None

#check for tie
def check_tie():
    global is_valid
    if "-" not in board:
        is_valid=False
        return True
    else:
        return False
#main function
play_game()
