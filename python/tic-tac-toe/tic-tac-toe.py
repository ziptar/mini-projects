import os
from random import randint


def clear_console():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    clear_console()
    print("+-----------+")
    for i in range(3):
        print("| ",board[i][0], " | ",board[i][1], " | ",board[i][2], " |", sep="")
        print("+-----------+")
    
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    global free_fields
    while True:
        input_key = input("Enter your move (one of the digits displayed), or 'q' to quit the game: ")
        if input_key == "q" or input_key == "Q":
            return False
        try:
            cell = int(input_key) - 1
            if cell < 0 or cell > 8 or cell == 4:
                display_board(board)
                continue
            row = cell // 3
            col = cell % 3
            if board[row][col] == "o" or board[row][col] == "x":
                display_board(board)
                continue
            board[row][col] = "o"
            free_fields = make_list_of_free_fields(board)
            display_board(board)
            return True
        except ValueError:
            display_board(board)            
        
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "x" and board[i][j] != "o":
                free_fields.append((i, j))
                                   
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game    
    filled_diag1_cells = 0
    filled_diag2_cells = 0
    for i in range(3):
        filled_row_cells = 0
        filled_col_cells = 0
        for j in range(3):
            if board[i][j] == sign:
                filled_row_cells += 1
            if board[j][i] == sign:
                filled_col_cells += 1
                
        if filled_row_cells == 3 or filled_col_cells == 3:
            return True
        if board[i][i] == sign:
            filled_diag1_cells += 1
        if board[i][2 - i] == sign:
            filled_diag2_cells += 1
    
    return filled_diag1_cells == 3 or filled_diag2_cells == 3       

def draw_move(board):
    # The function draws the computer's move and updates the board.  
    global free_fields  
    end = len(free_fields) - 1
    if end >= 0:
        r = randint(0, end)
    row, col = free_fields[r]
    board[row][col] = "x"
    free_fields = make_list_of_free_fields(board)
    display_board(board)
    
def victory_message(msg):
    print(msg)
    input("Press enter to play again.")

def game_over():
    clear_console()
    print("Game over.")

def initialize():
    global board
    global free_fields
    board = [["1", "2", "3"], ["4", "x", "6"], ["7", "8", "9"]]
    free_fields = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    display_board(board)

initialize()

while True:       
    if not enter_move(board):
        break
    if victory_for(board, "o"):
        victory_message("You win.")
        initialize()
    else:
        draw_move(board)
        if victory_for(board, "x"):
            victory_message("Computer wins.")
            initialize()
        else:  
            if len(free_fields) == 0:   
                victory_message("It's a tie.")    
                initialize()
      
game_over()      
        

