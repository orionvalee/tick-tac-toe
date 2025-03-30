# main.py
"""
Main Pygame application loop for graphical Tic-Tac-Toe.
Initializes Pygame, runs the event loop, and delegates game logic and drawing
to the Game class.
"""

import pygame
import sys

# Import the Game class and GUI drawing functions/constants
from game import Game
import gui # We need gui for constants like dimensions and drawing the button

# --- Constants ---
FPS = 30 # Frames per second
# -----------------

def main():
    """Main game function."""

    # --- Difficulty Selection (Console) ---
    difficulty = ""
    while difficulty not in ["easy", "hard"]:
        difficulty = input("Choose difficulty (easy/hard): ").lower().strip()
        if difficulty not in ["easy", "hard"]:
            print("Invalid choice. Please type 'easy' or 'hard'.")
    print(f"Difficulty set to: {difficulty}")
    # -------------------------------------

    pygame.init()
    # Use constants from gui module for screen dimensions
    screen = pygame.display.set_mode((gui.WIDTH, gui.HEIGHT))
    pygame.display.set_caption(f'Tic Tac Toe - Human (X) vs AI (O) - {difficulty.capitalize()}') # Add difficulty to title
    clock = pygame.time.Clock()

    # Create the game instance, passing the chosen difficulty
    game = Game(difficulty=difficulty)
    play_again_button_rect = None # Store button rect for click detection

    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            # Pass mouse clicks to the game object
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.game_over:
                    # Check if "Play Again" button was clicked
                    if play_again_button_rect and play_again_button_rect.collidepoint(event.pos):
                        print("Resetting game...")
                        game.reset()
                        play_again_button_rect = None # Clear button rect
                else:
                    # Let the game object handle the click during active play
                    game.handle_click(event.pos)

            # Handle the custom event for AI's turn
            if event.type == game.ai_move_event:
                game.handle_ai_turn()

        # --- Drawing ---
        screen.fill(gui.BG_COLOR) # Clear screen each frame

        # Let the game object handle drawing the game state (board, pieces, status/win msg)
        game.draw(screen)

        # Draw the "Play Again" button only if the game is over
        if game.game_over:
            play_again_button_rect = gui.draw_play_again_button(screen) # Draw and get rect
        else:
            play_again_button_rect = None # No button when game is active

        # --- Update Display ---
        pygame.display.update()
        clock.tick(FPS) # Limit frame rate

if __name__ == "__main__":
    main() 