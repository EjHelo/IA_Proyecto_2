import numpy as np

''' Constant variables '''
ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    ''' inicialize the matrix with zeros '''
    board = np.zeros((6,7))
    return board

def drop_piece(board, row, column, piece):
    ''' insert a piece on the board '''
    board[row][column] = piece

def is_valid_location(board, column):
    ''' verify iftop row (5) is empty '''
    return board[5][column] == 0

def get_next_open_row(board, column):
    ''' return the last empty position in the column '''
    for row in range(ROW_COUNT):
        if board[row][column] == 0:
            return row
    
def print_board(board):
    ''' flip the board '''
    print(np.flip(board, 0))

def winning_move(board, piece):
    ''' horizontal winning '''
    for col in range(COLUMN_COUNT-3):
        for row in range(ROW_COUNT):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece :
                return True

    ''' vertical winning '''
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT-3):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece :
                return True

    ''' diagonal winning '''
    for col in range(COLUMN_COUNT-3):
        for row in range(ROW_COUNT-3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece :
                return True
            
        for row in range(3, ROW_COUNT):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece :
                return True
            

board = create_board()
turn = 0
print(board)

while True:
    
    # Ask player 1 for a column selection 
    if turn == 0:
        column = int(input("Player 1 make your selection (0 -6): "))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 1)

            if winning_move(board, 1):
                print("Player 1 is the WINNER!!")
                break
            
        turn = 1
    
    # Ask player 2 for a column selection
    elif turn == 1:
        column = int(input("Player 2 make your selection (0 -6): "))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)

            if winning_move(board, 2):
                print("Player 2 is the WINNER!!")
                break
        turn = 0
    print_board(board)

    
print_board(board)
print("The game has finished !")
