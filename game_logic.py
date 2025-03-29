# game_logic.py

"""
Contains the core logic for determining game state (win/draw)
and managing player turns.
"""

# Define all possible winning combinations (indices in the flat list)
WINNING_COMBINATIONS = [
    # Rows
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    # Columns
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    # Diagonals
    (0, 4, 8), (2, 4, 6)
]

def check_win(board, mark):
    """Checks if the given player ('X' or 'O') has won the game."""
    for combo in WINNING_COMBINATIONS:
        if all(board[i] == mark for i in combo):
            return True
    return False

def check_draw(board):
    """Checks if the game is a draw (board is full and no one has won)."""
    # Note: This function assumes check_win has already been called for the last player
    # in the main game loop. A draw occurs if the board is full AND there's no winner.
    # The is_board_full check is sufficient here because the main loop handles the win check first.
    from board import is_board_full # Local import to avoid circular dependency issues if needed later
    return is_board_full(board)

def switch_player(current_player):
    """Switches the current player."""
    return 'O' if current_player == 'X' else 'X'