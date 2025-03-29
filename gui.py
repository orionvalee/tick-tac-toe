# gui.py
"""
Handles all Pygame drawing operations and GUI constants.
"""

import pygame

# --- Constants ---
# Screen dimensions
WIDTH, HEIGHT = 450, 550  # Increased height for status message
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS # // for integer division

# Circle dimensions (O)
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15

# Cross dimensions (X)
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4 # Padding inside square for X

# Colors (RGB)
BG_COLOR = (28, 170, 156) # Teal-ish background
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200) # Off-white
CROSS_COLOR = (66, 66, 66)   # Dark grey
TEXT_COLOR = (10, 80, 74)
GAMEOVER_COLOR = (220, 20, 60) # Crimson for game over text
BUTTON_COLOR = (211, 211, 211) # Light grey
BUTTON_TEXT_COLOR = (0, 0, 0)   # Black
HIGHLIGHT_COLOR = (255, 255, 0, 150) # Yellow, semi-transparent for winning line

# Fonts
pygame.font.init() # Initialize font module
STATUS_FONT = pygame.font.SysFont('consolas', 30, bold=True)
GAMEOVER_FONT = pygame.font.SysFont('impact', 50)
BUTTON_FONT = pygame.font.SysFont('arial', 25)
# -----------------

def draw_lines(screen):
    """Draws the Tic-Tac-Toe grid lines."""
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH) # Adjusted height
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH)

def draw_figures(screen, board):
    """Draws X's and O's based on the board state."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            index = row * BOARD_COLS + col
            if board[index] == 'O':
                # Draw Circle (O) - center calculation is key
                center_x = int(col * SQUARE_SIZE + SQUARE_SIZE // 2)
                center_y = int(row * SQUARE_SIZE + SQUARE_SIZE // 2)
                pygame.draw.circle(screen, CIRCLE_COLOR, (center_x, center_y), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[index] == 'X':
                # Draw Cross (X) - requires two lines
                # Top-left to bottom-right
                start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                # Top-right to bottom-left
                start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

def draw_status(screen, message):
    """Displays the current game status (whose turn)."""
    text = STATUS_FONT.render(message, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 50)) # Position at the bottom center
    # Add a background rectangle for better visibility
    bg_rect = pygame.Rect(0, HEIGHT - 100, WIDTH, 100)
    pygame.draw.rect(screen, LINE_COLOR, bg_rect) # Use line color for status background
    screen.blit(text, text_rect)

def draw_winning_line(screen, start_pos, end_pos):
    """Draws a line through the winning combination."""
    if start_pos and end_pos:
        # Create a slightly transparent surface for the line
        line_surf = pygame.Surface((WIDTH, HEIGHT - 100), pygame.SRCALPHA) # Use SRCALPHA for transparency
        pygame.draw.line(line_surf, HIGHLIGHT_COLOR, start_pos, end_pos, LINE_WIDTH + 5)
        screen.blit(line_surf, (0,0))


def get_win_line_coords(row_or_col_or_diag_index, win_type):
    """Calculates start and end coordinates for the winning line."""
    half_sq = SQUARE_SIZE // 2

    if win_type == 'row':
        y = row_or_col_or_diag_index * SQUARE_SIZE + half_sq
        start_pos = (half_sq // 2, y)
        end_pos = (WIDTH - half_sq // 2, y)
    elif win_type == 'col':
        x = row_or_col_or_diag_index * SQUARE_SIZE + half_sq
        start_pos = (x, half_sq // 2)
        end_pos = (x, HEIGHT - 100 - half_sq // 2) # Adjusted height
    elif win_type == 'diag1': # Top-left to bottom-right
        start_pos = (half_sq // 2, half_sq // 2)
        end_pos = (WIDTH - half_sq // 2, HEIGHT - 100 - half_sq // 2)
    elif win_type == 'diag2': # Top-right to bottom-left
        start_pos = (WIDTH - half_sq // 2, half_sq // 2)
        end_pos = (half_sq // 2, HEIGHT - 100 - half_sq // 2)
    else:
        return None, None

    return start_pos, end_pos


def draw_game_over(screen, message, winning_line_info):
    """Displays the game over message and highlights the win."""

    # Draw semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT - 100), pygame.SRCALPHA)
    overlay.fill((40, 40, 40, 180)) # Dark grey, semi-transparent
    screen.blit(overlay, (0, 0))

    # Draw winning line if applicable
    if winning_line_info:
        win_type, index = winning_line_info
        start_pos, end_pos = get_win_line_coords(index, win_type)
        draw_winning_line(screen, start_pos, end_pos)

    # Draw game over text
    text = GAMEOVER_FONT.render(message, True, GAMEOVER_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, (HEIGHT - 100) // 2)) # Center on game board area
    screen.blit(text, text_rect)

def draw_play_again_button(screen):
    """Draws the 'Play Again?' button and returns its Rect."""
    button_width = 180
    button_height = 50
    button_x = (WIDTH - button_width) // 2
    button_y = HEIGHT - 75 # Position below status area

    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect, border_radius=10)

    button_text = BUTTON_FONT.render("Play Again?", True, BUTTON_TEXT_COLOR)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    return button_rect # Return the rect for click detection