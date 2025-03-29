# board.py

"""
Manages the Tic-Tac-Toe game board state and display.
"""

def initialize_board():
    """Creates and returns an empty 3x3 Tic-Tac-Toe board."""
    return [' ' for _ in range(9)] # Represents the 3x3 board as a flat list

def display_board(board):
    """Displays the current state of the board in a visually appealing format."""
    print("\n     TIC TAC TOE")
    print("-------------------")
    print(f"|  {board[0]}  |  {board[1]}  |  {board[2]}  |")
    print("-------------------")
    print(f"|  {board[3]}  |  {board[4]}  |  {board[5]}  |")
    print("-------------------")
    print(f"|  {board[6]}  |  {board[7]}  |  {board[8]}  |")
    print("-------------------\n")
    # Display guide numbers for user input
    print("   (Positions:)")
    print("-------------------")
    print("|  1  |  2  |  3  |")
    print("-------------------")
    print("|  4  |  5  |  6  |")
    print("-------------------")
    print("|  7  |  8  |  9  |")
    print("-------------------\n")


def is_cell_empty(board, position):
    """Checks if the cell at the given position (1-9) is empty."""
    # Adjust position to be 0-indexed for list access
    return board[position - 1] == ' '

def place_mark(board, position, mark):
    """Places the player's mark ('X' or 'O') on the board at the given position."""
    # Adjust position to be 0-indexed
    if 1 <= position <= 9 and is_cell_empty(board, position):
        board[position - 1] = mark
        return True
    return False # Indicate failure if position is invalid or taken

def is_board_full(board):
    """Checks if the board has any empty cells left."""
    return ' ' not in board