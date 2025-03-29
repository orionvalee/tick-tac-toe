# main.py

"""
The main entry point for the Tic-Tac-Toe game (Human vs AI).
Orchestrates the game flow using functions from other modules.
"""

import os
import time
import sys
import random

# Import functions from our other modules
from board import initialize_board, display_board, place_mark, is_board_full
from game_logic import check_win, check_draw, switch_player
from player import get_player_move, get_ai_move # Import both move functions

# --- Constants ---
HUMAN_PLAYER = 'X'
AI_PLAYER = 'O'
# -----------------

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome_message():
    """Prints a stylish welcome message for Human vs AI."""
    clear_screen()
    print("***********************************")
    print("*                                 *")
    print("*   Welcome to Terminal Tic Tac Toe! *")
    print("*         (Human vs AI)           *")
    print("*                                 *")
    print("***********************************")
    print(f"\nYou are Player '{HUMAN_PLAYER}'. The AI is Player '{AI_PLAYER}'.")
    print("Enter a number (1-9) to place your mark.")
    time.sleep(3.5) # Pause for effect

def print_game_over_message(winner=None):
    """Prints the final result of the game."""
    if winner == HUMAN_PLAYER:
        print(f"🎉 Congratulations! You ({winner}) beat the AI! 🎉")
    elif winner == AI_PLAYER:
        print(f"🤖 Oh no! The AI ({winner}) won this time. 🤖")
    else:
        print("🤝 It's a draw! Well played. 🤝")
    print("\n***********************************")
    print("*          Game Over            *")
    print("***********************************\n")


def game():
    """Runs a single round of Tic-Tac-Toe between Human and AI."""
    board = initialize_board()
    # Randomly decide who goes first, or let Human start
    # current_player = random.choice([HUMAN_PLAYER, AI_PLAYER])
    current_player = HUMAN_PLAYER # Let Human always start for simplicity
    print(f"\nPlayer '{current_player}' will go first.")
    time.sleep(2)

    game_over = False
    winner = None

    while not game_over:
        clear_screen()
        display_board(board)

        if current_player == HUMAN_PLAYER:
            # Get move from the human player
            position = get_player_move(board, HUMAN_PLAYER)
        else:
            # Get move from the AI
            position = get_ai_move(board, AI_PLAYER, HUMAN_PLAYER)
            if position is None: # Handle potential AI error
                 print("Critical AI Error - Ending game.")
                 game_over = True
                 continue # Skip rest of the loop iteration
            print(f"AI ({AI_PLAYER}) chooses position {position}")
            time.sleep(1) # Pause briefly after AI move announcement

        # Place the mark on the board
        if place_mark(board, position, current_player):
            # Check for win ONLY after a successful mark placement
            if check_win(board, current_player):
                winner = current_player
                game_over = True
            # Check for draw (only if no win)
            elif is_board_full(board): # Use is_board_full directly here
                game_over = True
            # Switch player if game is not over
            else:
                current_player = switch_player(current_player, HUMAN_PLAYER, AI_PLAYER)
        else:
             # This case should ideally not happen with validation in place,
             # but good for robustness, especially if AI logic had a bug.
             print("Error placing mark. Please check game logic.")
             time.sleep(2)


    # Game finished, display final board and result
    clear_screen()
    display_board(board)
    print_game_over_message(winner)


def main():
    """Main function to run the game and handle replays."""
    print_welcome_message()
    while True:
        game() # Play one round

        # Ask to play again
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye 👋")
            break
        else:
             print("\nStarting a new game...\n")
             time.sleep(2)


# Standard Python entry point check
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user. Goodbye! 👋")
        sys.exit(0) # Exit gracefully on Ctrl+C