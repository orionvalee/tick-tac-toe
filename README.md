# Graphical Tic Tac Toe (Human vs AI) using Pygame

A graphical Tic Tac Toe game implemented in Python using the Pygame library. This version features a Human player ('X') against a rule-based AI opponent ('O'). The project maintains a modular structure.

## Features

*   **Graphical Interface:** Uses Pygame for visual display and mouse input.
*   **Human vs. AI Gameplay:** Play against a rule-based AI.
*   **Clear Visuals:** Displays the grid, X's, O's, current turn, and game over status.
*   **Win Highlighting:** The winning line (row, column, or diagonal) is highlighted upon victory.
*   **Rule-Based AI Opponent:** The AI attempts to win, block, and make strategic moves (center, corners, sides).
*   **Play Again:** Option to restart the game after it ends.
*   **Modular Design:** Code is separated into modules for logic, board state, AI, and GUI drawing.

## Project Structure

*   `main_gui.py`: The main Pygame application loop. Handles initialization, events (mouse clicks, quit), game state management, and calls other modules.
*   `board.py`: Manages the internal representation of the game board state (list of ' ', 'X', 'O').
*   `game_logic.py`: Contains the core rules: checking for wins (and identifying the winning line), detecting draws, and switching players.
*   `player.py`: Contains the logic for the AI opponent's move selection.
*   `gui.py`: Contains all Pygame-specific drawing functions (grid, figures, text, buttons) and visual constants (colors, sizes, fonts).
*   `README.md`: This file.

## Requirements

*   Python 3.x
*   Pygame library: Install using `pip install pygame`

## How to Run

1.  **Ensure you have Python 3 installed.**
2.  **Install Pygame:** Open your terminal or command prompt and run:
    ```bash
    pip install pygame
    ```
3.  **Save the files:** Make sure all the `.py` files (`main_gui.py`, `board.py`, `game_logic.py`, `player.py`, `gui.py`) are in the same directory (e.g., `tic_tac_toe_gui`).
4.  **Open your terminal or command prompt.**
5.  **Navigate to the directory** where you saved the files:
    ```bash
    cd path/to/your/tic_tac_toe_gui_folder
    ```
6.  **Run the main script:**
    ```bash
    python main_gui.py
    ```
7.  A Pygame window should open. Click on an empty square to make your move as Player 'X'. The AI ('O') will automatically take its turn. Click "Play Again?" after the game finishes to start a new round.

## Gameplay

*   The Human player ('X') always starts.
*   Click on an empty square on the grid during your turn.
*   The AI ('O') will calculate and make its move after a short delay.
*   The game ends when a player gets three marks in a row or the board is full (draw).
*   The winning line is highlighted.
*   Click the "Play Again?" button to restart.