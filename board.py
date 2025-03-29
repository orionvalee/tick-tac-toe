# board.py
"""
Manages the Tic-Tac-Toe internal game board state.
"""

def initialize_board():
    """Creates and returns an empty 3x3 Tic-Tac-Toe board."""
    return [' ' for _ in range(9)] # Represents the 3x3 board as a flat list

def is_cell_empty(board, position):
    """Checks if the cell at the given position (1-9) is empty."""
    if 1 <= position <= 9:
        return board[position - 1] == ' '
    return False

def place_mark(board, position, mark):
    """Places the player's mark ('X' or 'O') on the board at the given position."""
    if 1 <= position <= 9 and is_cell_empty(board, position):
        board[position - 1] = mark
        return True
    return False

def get_empty_cells(board):
    """Returns a list of indices (0-8) of empty cells."""
    return [i for i, cell in enumerate(board) if cell == ' ']

def is_board_full(board):
    """Checks if the board has any empty cells left."""
    return ' ' not in board