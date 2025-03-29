# game_logic.py
"""
Contains the core logic for determining game state (win/draw)
and managing player turns.
"""
from board import is_board_full

# Define all possible winning combinations (indices in the flat list)
# Store them with type and index for easier GUI highlighting
WINNING_COMBINATIONS_INFO = [
    # Rows (type, index, combo_tuple)
    ('row', 0, (0, 1, 2)), ('row', 1, (3, 4, 5)), ('row', 2, (6, 7, 8)),
    # Columns
    ('col', 0, (0, 3, 6)), ('col', 1, (1, 4, 7)), ('col', 2, (2, 5, 8)),
    # Diagonals
    ('diag1', 0, (0, 4, 8)), ('diag2', 1, (2, 4, 6)) # Use index 0 for diag1, 1 for diag2
]

def check_win(board, mark):
    """
    Checks if the given player ('X' or 'O') has won the game.
    Returns tuple (win_type, index) if win, else None.
    """
    for win_type, index, combo in WINNING_COMBINATIONS_INFO:
        if all(board[i] == mark for i in combo):
            return (win_type, index) # Return info needed for highlighting
    return None # No win found

def check_draw(board):
    """Checks if the game is a draw (board is full and no one has won)."""
    # Assumes check_win failed for the last player
    return is_board_full(board)

def switch_player(current_player, human_mark, ai_mark):
    """Switches the current player between human and AI."""
    return ai_mark if current_player == human_mark else human_mark