# player.py
"""
Handles determining the AI's move. Human input is handled in main_gui.py.
"""
import random
import time

# Need to import from the correct modules now
from board import is_cell_empty, get_empty_cells
from game_logic import check_win as check_win_logic # Rename to avoid clash if needed

# --- AI Logic (same as before) ---
def get_ai_move(board, ai_mark, human_mark):
    """Determines the AI's next move using a rule-based strategy."""
    print(f"AI ({ai_mark}) is thinking...") # Keep console log for debugging
    # No sleep here, makes GUI feel sluggish. Add delay in main loop if desired.

    empty_cells_indices = get_empty_cells(board) # Get 0-based indices

    # 1. Check if AI can win
    for index in empty_cells_indices:
        temp_board = board[:]
        temp_board[index] = ai_mark
        if check_win_logic(temp_board, ai_mark): # Use the imported check_win
            print(f"AI chooses winning move: {index + 1}")
            return index + 1 # Return 1-based position

    # 2. Check if Human can win and block
    for index in empty_cells_indices:
        temp_board = board[:]
        temp_board[index] = human_mark
        if check_win_logic(temp_board, human_mark):
             print(f"AI blocks human at: {index + 1}")
             return index + 1

    # 3. Try center
    center_index = 4
    if center_index in empty_cells_indices:
        print("AI takes center")
        return center_index + 1

    # 4. Try corners
    corner_indices = [0, 2, 6, 8]
    available_corners = [i for i in corner_indices if i in empty_cells_indices]
    if available_corners:
        move = random.choice(available_corners)
        print(f"AI takes corner: {move + 1}")
        return move + 1

    # 5. Try sides
    side_indices = [1, 3, 5, 7]
    available_sides = [i for i in side_indices if i in empty_cells_indices]
    if available_sides:
        move = random.choice(available_sides)
        print(f"AI takes side: {move + 1}")
        return move + 1

    # Fallback (shouldn't happen in standard play)
    if empty_cells_indices:
        move = random.choice(empty_cells_indices)
        print(f"AI takes random available: {move + 1}")
        return move + 1
    else:
        print("Error: AI couldn't find a valid move.")
        return None