"""
Contains the Game class that manages the overall state and flow of Tic-Tac-Toe.
"""

import pygame # Needed for timer event

# Import game components
from board import initialize_board, place_mark, is_cell_empty
from game_logic import check_win, check_draw
from ai_player import get_ai_move
import gui # Might need constants from here initially

# Player marks (can be moved to constants.py later)
HUMAN_PLAYER = 'X'
AI_PLAYER = 'O'
AI_DELAY_MS = 500 # Delay before AI makes a move

class Game:
    """Manages the Tic-Tac-Toe game state and logic."""
    def __init__(self, difficulty="hard"):
        """Initializes a new game."""
        self.board = initialize_board()
        self.current_player = HUMAN_PLAYER # Human starts
        self.game_over = False
        self.winner = None
        self.winning_line_info = None # (type, index) or None
        self.ai_move_event = pygame.USEREVENT + 1 # Custom event for AI move timer
        self.difficulty = difficulty # Store the difficulty

    def reset(self):
        """Resets the game to the initial state."""
        self.board = initialize_board()
        self.current_player = HUMAN_PLAYER
        self.game_over = False
        self.winner = None
        self.winning_line_info = None
        # We keep the difficulty selected for the session unless changed elsewhere
        pygame.time.set_timer(self.ai_move_event, 0)

    def handle_click(self, pos):
        """Handles a mouse click event at the given (x, y) position."""
        if self.game_over or self.current_player != HUMAN_PLAYER:
            return # Ignore clicks if game over or not human's turn

        clicked_position = self._get_clicked_board_pos(pos)
        if clicked_position and is_cell_empty(self.board, clicked_position):
            self._make_move(clicked_position, HUMAN_PLAYER)

    def _get_clicked_board_pos(self, pos):
        """Converts mouse click coordinates (x, y) to board position (1-9)."""
        x, y = pos
        # Check if click is within the board area (adjust based on gui constants)
        if y > gui.HEIGHT - 100: # Example: Clicked below board/status area
            return None

        # Assuming gui.SQUARE_SIZE, gui.BOARD_ROWS, gui.BOARD_COLS are available
        row = y // gui.SQUARE_SIZE
        col = x // gui.SQUARE_SIZE

        if 0 <= row < gui.BOARD_ROWS and 0 <= col < gui.BOARD_COLS:
            return row * gui.BOARD_COLS + col + 1
        else:
            return None

    def _make_move(self, position, player):
        """Places a mark on the board and checks the game status."""
        if place_mark(self.board, position, player):
            win_info = check_win(self.board, player)
            if win_info:
                self.winner = player
                self.winning_line_info = win_info
                self.game_over = True
                print(f"Game Over! Winner: {self.winner}")
            elif check_draw(self.board):
                self.game_over = True
                print("Game Over! It's a Draw!")
            else:
                self._switch_player()

    def _switch_player(self):
        """Switches the current player and triggers AI move if necessary."""
        if self.current_player == HUMAN_PLAYER:
            self.current_player = AI_PLAYER
            # Start a timer for the AI's move
            pygame.time.set_timer(self.ai_move_event, AI_DELAY_MS, 1) # 1 means run once
            print(f"Switched to AI ({AI_PLAYER}). Starting timer.")
        else:
            self.current_player = HUMAN_PLAYER
            print(f"Switched to Human ({HUMAN_PLAYER}).")


    def handle_ai_turn(self):
        """Handles the AI's turn when triggered by the timer event."""
        if not self.game_over and self.current_player == AI_PLAYER:
            # Pass the stored difficulty to the AI
            ai_position = get_ai_move(self.board, AI_PLAYER, HUMAN_PLAYER, self.difficulty)
            if ai_position:
                print(f"AI ({self.difficulty}) chooses position {ai_position}") # Log difficulty
                self._make_move(ai_position, AI_PLAYER)
            else:
                # Handle case where AI fails to move (should not happen)
                print("Error: AI failed to find a valid move.")
                self.game_over = True # Force game over? Or maybe a draw?

    def draw(self, screen):
        """Calls the GUI functions to draw the current game state."""
        # Clear screen (might be done in main loop)
        # screen.fill(gui.BG_COLOR) # Decide if clearing happens here or in main.py

        gui.draw_lines(screen)
        gui.draw_figures(screen, self.board)

        if self.game_over:
            message = f"Player {self.winner} Wins!" if self.winner else "It's a Draw!"
            gui.draw_game_over(screen, message, self.winning_line_info)
            # The button drawing/rect handling might stay in main.py or move here
            # play_again_button_rect = gui.draw_play_again_button(screen)
            # return play_again_button_rect # Return rect if needed by main
        else:
            status_message = f"Player {self.current_player}'s Turn"
            gui.draw_status(screen, status_message)
        # return None # Return None if no button rect needed 