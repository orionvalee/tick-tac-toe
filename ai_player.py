# player.py
"""
Handles determining the AI's move. Human input is handled in main_gui.py.
"""
import random
import time

# Need to import from the correct modules now
from board import is_cell_empty, get_empty_cells
from game_logic import check_win as check_win_logic # Rename to avoid clash if needed

# --- AI Logic ---
def get_ai_move(board, ai_mark, human_mark, difficulty="hard"): # Add difficulty parameter with default
    """Determines the AI's next move based on the chosen difficulty."""
    print(f"AI ({ai_mark}) thinking (Difficulty: {difficulty})...") # Add difficulty to log

    empty_cells_indices = get_empty_cells(board) # Get 0-based indices

    if not empty_cells_indices:
        print("Error: AI couldn't find a valid move (no empty cells).")
        return None # No moves possible

    # --- Easy Difficulty ---
    if difficulty == "easy":
        move_index = random.choice(empty_cells_indices)
        print(f"AI (Easy) chooses random move: {move_index + 1}")
        return move_index + 1 # Return 1-based position

    # --- Hard Difficulty (Existing Logic) ---
    elif difficulty == "hard":
        # 1. Check if AI can win
        for index in empty_cells_indices:
            temp_board = board[:]
            temp_board[index] = ai_mark
            if check_win_logic(temp_board, ai_mark): # Use the imported check_win
                print(f"AI (Hard) chooses winning move: {index + 1}")
                return index + 1 # Return 1-based position

        # 2. Check if Human can win and block
        for index in empty_cells_indices:
            temp_board = board[:]
            temp_board[index] = human_mark
            if check_win_logic(temp_board, human_mark):
                 print(f"AI (Hard) blocks human at: {index + 1}")
                 return index + 1

        # 3. Try center
        center_index = 4
        if center_index in empty_cells_indices:
            print("AI (Hard) takes center")
            return center_index + 1

        # 4. Try corners
        corner_indices = [0, 2, 6, 8]
        available_corners = [i for i in corner_indices if i in empty_cells_indices]
        if available_corners:
            move = random.choice(available_corners) # Keep random choice among corners
            print(f"AI (Hard) takes corner: {move + 1}")
            return move + 1

        # 5. Try sides
        side_indices = [1, 3, 5, 7]
        available_sides = [i for i in side_indices if i in empty_cells_indices]
        if available_sides:
            move = random.choice(available_sides) # Keep random choice among sides
            print(f"AI (Hard) takes side: {move + 1}")
            return move + 1

        # Fallback (Should only happen if board is full, handled above)
        # If we reach here with empty cells, something is wrong, but let's be safe
        print(f"AI (Hard) choosing random from remaining: {empty_cells_indices}")
        move_index = random.choice(empty_cells_indices)
        return move_index + 1

    else:
        # Fallback for unknown difficulty - default to easy? Or raise error?
        print(f"Warning: Unknown difficulty '{difficulty}'. Defaulting to easy.")
        move_index = random.choice(empty_cells_indices)
        return move_index + 1 