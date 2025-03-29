# main_gui.py
"""
Main Pygame application loop for graphical Tic-Tac-Toe (Human vs AI).
Handles events, game state, drawing calls, and AI interaction.
"""

import pygame
import sys
import time

# Import game components
from board import initialize_board, place_mark, is_cell_empty
from game_logic import check_win, check_draw, switch_player
from player import get_ai_move
# Import GUI components and constants
import gui

# --- Constants ---
HUMAN_PLAYER = 'X'
AI_PLAYER = 'O'
FPS = 30 # Frames per second
# -----------------

def get_clicked_pos(pos):
    """Converts mouse click coordinates (x, y) to board position (1-9)."""
    x, y = pos
    # Check if click is within the board area
    if y > gui.HEIGHT - 100: # Clicked below board
        return None

    row = y // gui.SQUARE_SIZE
    col = x // gui.SQUARE_SIZE

    # Ensure row and col are within bounds (0, 1, 2)
    if 0 <= row < gui.BOARD_ROWS and 0 <= col < gui.BOARD_COLS:
        # Convert 0-based row/col to 1-based position
        return row * gui.BOARD_COLS + col + 1
    else:
        return None # Click outside valid grid squares

def reset_game():
    """Resets the game state for a new round."""
    board = initialize_board()
    current_player = HUMAN_PLAYER # Human always starts in this version
    game_over = False
    winner = None
    winning_line_info = None # Tuple (type, index) or None
    return board, current_player, game_over, winner, winning_line_info

def main():
    """Main game function."""
    pygame.init()
    screen = pygame.display.set_mode((gui.WIDTH, gui.HEIGHT))
    pygame.display.set_caption('Tic Tac Toe - Human (X) vs AI (O)')
    clock = pygame.time.Clock()

    board, current_player, game_over, winner, winning_line_info = reset_game()
    play_again_button_rect = None # Store button rect for click detection

    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if current_player == HUMAN_PLAYER:
                    clicked_position = get_clicked_pos(event.pos)

                    if clicked_position and is_cell_empty(board, clicked_position):
                        if place_mark(board, clicked_position, HUMAN_PLAYER):
                            # Check for win/draw after human move
                            win_info = check_win(board, HUMAN_PLAYER)
                            if win_info:
                                winner = HUMAN_PLAYER
                                winning_line_info = win_info
                                game_over = True
                            elif check_draw(board):
                                game_over = True # It's a draw
                            else:
                                # Switch to AI player
                                current_player = switch_player(current_player, HUMAN_PLAYER, AI_PLAYER)
                                pygame.time.set_timer(pygame.USEREVENT, 500, 1) # Trigger AI move after 500ms

            elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                 # Check if "Play Again" button was clicked
                 if play_again_button_rect and play_again_button_rect.collidepoint(event.pos):
                     print("Resetting game...")
                     board, current_player, game_over, winner, winning_line_info = reset_game()
                     play_again_button_rect = None # Clear button rect

            # --- AI Turn Trigger ---
            if event.type == pygame.USEREVENT and not game_over and current_player == AI_PLAYER:
                 ai_position = get_ai_move(board, AI_PLAYER, HUMAN_PLAYER)
                 if ai_position and place_mark(board, ai_position, AI_PLAYER):
                      # Check for win/draw after AI move
                      win_info = check_win(board, AI_PLAYER)
                      if win_info:
                          winner = AI_PLAYER
                          winning_line_info = win_info
                          game_over = True
                      elif check_draw(board):
                          game_over = True # It's a draw
                      else:
                          # Switch back to Human player
                          current_player = switch_player(current_player, HUMAN_PLAYER, AI_PLAYER)
                 else:
                     # Handle case where AI fails to move (should not happen in normal play)
                     print("AI move failed or invalid position returned.")
                     # Optionally, force a draw or handle error
                     game_over = True


        # --- Drawing ---
        screen.fill(gui.BG_COLOR)
        gui.draw_lines(screen)
        gui.draw_figures(screen, board)

        # Display status or game over message
        if game_over:
            message = ""
            if winner:
                message = f"Player {winner} Wins!"
            else:
                message = "It's a Draw!"
            gui.draw_game_over(screen, message, winning_line_info)
            play_again_button_rect = gui.draw_play_again_button(screen) # Draw and get rect
        else:
            status_message = f"Player {current_player}'s Turn"
            gui.draw_status(screen, status_message)
            play_again_button_rect = None # No button when game is active

        # --- Update Display ---
        pygame.display.update()
        clock.tick(FPS) # Limit frame rate

if __name__ == "__main__":
    main()