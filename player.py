# player.py

"""
Handles getting valid input from the human player and determining the AI's move.
"""
import random
import time

from board import is_cell_empty, get_empty_cells # Need access to board state
from game_logic import check_win # Need access to win checking for AI strategy

def get_player_move(board, player_mark):
    """Prompts the human player for their move and validates the input."""
    while True:
        try:
            move_input = input(f"Your turn ({player_mark}), enter your move (1-9): ")
            position = int(move_input)

            if not 1 <= position <= 9:
                print("❗️ Invalid input: Position must be between 1 and 9.")
            elif not is_cell_empty(board, position):
                print("❗️ Invalid input: That cell is already taken!")
            else:
                return position # Valid move received

        except ValueError:
            print("❗️ Invalid input: Please enter a number (1-9).")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def get_ai_move(board, ai_mark, human_mark):
    """Determines the AI's next move using a rule-based strategy."""
    print(f"AI ({ai_mark}) is thinking...", end='', flush=True)
    time.sleep(random.uniform(0.5, 1.2)) # Simulate thinking time
    print(" done.")

    empty_cells_indices = get_empty_cells(board) # Get 0-based indices

    # --- AI Strategy ---

    # 1. Check if AI can win in the next move
    for index in empty_cells_indices:
        temp_board = board[:] # Create a copy
        temp_board[index] = ai_mark
        if check_win(temp_board, ai_mark):
            return index + 1 # Return 1-based position

    # 2. Check if Human can win in the next move, and block them
    for index in empty_cells_indices:
        temp_board = board[:] # Create a copy
        temp_board[index] = human_mark
        if check_win(temp_board, human_mark):
            return index + 1 # Return 1-based position

    # 3. Try to take the center (position 5, index 4)
    center_index = 4
    if center_index in empty_cells_indices:
        return center_index + 1

    # 4. Try to take a corner (positions 1, 3, 7, 9 -- indices 0, 2, 6, 8)
    corner_indices = [0, 2, 6, 8]
    available_corners = [i for i in corner_indices if i in empty_cells_indices]
    if available_corners:
        return random.choice(available_corners) + 1 # Choose a random available corner

    # 5. Try to take a side (positions 2, 4, 6, 8 -- indices 1, 3, 5, 7)
    side_indices = [1, 3, 5, 7]
    available_sides = [i for i in side_indices if i in empty_cells_indices]
    if available_sides:
        return random.choice(available_sides) + 1 # Choose a random available side

    # 6. Fallback (shouldn't technically be needed if logic above is sound, but safe)
    # This case would only happen if somehow the board is full but no win/draw detected yet,
    # or if get_empty_cells returned empty when it shouldn't.
    if empty_cells_indices:
         return random.choice(empty_cells_indices) + 1
    else:
         # This state should ideally not be reached in a valid game sequence
         print("Error: AI couldn't find a valid move.")
         return None # Indicate an error or unexpected state