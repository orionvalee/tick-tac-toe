# player.py

"""
Handles getting valid input from the human player.
"""

from board import is_cell_empty # Import necessary check from board module

def get_player_move(board, player_mark):
    """Prompts the current player for their move and validates the input."""
    while True:
        try:
            move_input = input(f"Player '{player_mark}', enter your move (1-9): ")
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
            print(f"An unexpected error occurred: {e}") # Catch other potential issues