# Terminal Tic Tac Toe (Human vs AI)

A simple, text-based Tic Tac Toe game implemented in Python, designed to run in the terminal. This version features a Human player against a rule-based AI opponent. The project demonstrates modular programming principles by separating concerns into different files.

## Features

*   Classic Tic Tac Toe gameplay: Human ('X') vs. AI ('O').
*   **Rule-Based AI Opponent:** The AI attempts to:
    1.  Win if possible.
    2.  Block the human player from winning.
    3.  Take the center square.
    4.  Take a corner square.
    5.  Take a side square.
*   Clear, formatted terminal display.
*   Input validation for the human player's moves.
*   Win and Draw detection.
*   Option to play again after a game ends.
*   "Smart" look with screen clearing, formatted output, and simulated AI thinking time.

## Project Structure

The project is organized into the following Python modules:

*   `main.py`: The main entry point of the application. It controls the overall game flow (Human vs AI turns), handles playing again, and orchestrates calls to other modules.
*   `board.py`: Manages the game board's state (creation, updating, checking empty cells) and is responsible for displaying the board in the terminal.
*   `game_logic.py`: Contains the core rules of Tic Tac Toe, including functions to check for winning conditions, detect draws, and switch players.
*   `player.py`: Handles user interaction for the human player and contains the logic for the AI opponent's move selection.
*   `README.md`: This file, providing information about the project.

## Requirements

*   Python 3.x

## How to Run

1.  **Ensure you have Python 3 installed.**
2.  **Save the files:** Make sure all the `.py` files (`main.py`, `board.py`, `game_logic.py`, `player.py`) are in the same directory (e.g., a folder named `tic_tac_toe_ai`).
3.  **Open your terminal or command prompt.**
4.  **Navigate to the directory** where you saved the files using the `cd` command.
    ```bash
    cd path/to/your/tic_tac_toe_ai_folder
    ```
5.  **Run the main script:**
    ```bash
    python main.py
    ```
6.  Follow the on-screen prompts to play the game! As the Human player ('X'), enter numbers 1-9 corresponding to the positions on the board when it's your turn. The AI ('O') will make its moves automatically.

## Gameplay

*   The Human player is 'X', the AI is 'O'. Player 'X' starts the first game.
*   The Human player enters a number from 1 to 9 to place their mark ('X') on the corresponding empty cell.
*   The AI ('O') automatically determines its move based on its strategy and places its mark.
*   The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
*   If all cells are filled and no player has won, the game is a draw.