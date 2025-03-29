# main.py

"""
The main entry point for the Tic-Tac-Toe game.
Orchestrates the game flow using functions from other modules.
"""

import os
import time
import sys

# Import functions from our other modules
from board import initialize_board, display_board, place_mark
from game_logic import check_win, check_draw, switch_player
from player import get_player_move

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome_message():
    """Prints a stylish welcome message."""
    clear_screen()
    print("***********************************")
    print("*                                 *")
    print("*   Welcome to Terminal Tic Tac Toe! *")
    print("*                                 *")
    print("***********************************")
    print("\nPlayer X goes first. Enter a number (1-9) to place your mark.")
    time.sleep(3) # Pause for effect

def print_game_over_message(winner=None):
    """Prints the final result of the game."""
    if winner:
        print(f"🎉 Congratulations Player '{winner}'! You win! 🎉")
    else:
        print("🤝 It's a draw! Well played by both sides. 🤝")
    print("\n***********************************")
    print("*          Game Over            *")
    print("***********************************\n")


def game():
    """Runs a single round of Tic-Tac-Toe."""
    board = initialize_board()
    current_player = 'X'
    game_over = False
    winner = None

    while not game_over:
        clear_screen()
        display_board(board)

        # Get move from the current player
        position = get_player_move(board, current_player)

        # Place the mark on the board
        place_mark(board, position, current_player)

        # Check for win
        if check_win(board, current_player):
            winner = current_player
            game_over = True
        # Check for draw (only if no win)
        elif check_draw(board):
            game_over = True
        # Switch player if game is not over
        else:
            current_player = switch_player(current_player)

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