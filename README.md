# Terminal Tic Tac Toe

A simple, text-based Tic Tac Toe game implemented in Python, designed to run in the terminal. This project demonstrates modular programming principles by separating concerns into different files.

## Features

*   Classic Tic Tac Toe gameplay for two human players.
*   Clear, formatted terminal display.
*   Input validation for player moves.
*   Win and Draw detection.
*   Option to play again after a game ends.
*   "Smart" look with screen clearing and formatted output.

## Project Structure

The project is organized into the following Python modules:

*   `main.py`: The main entry point of the application. It controls the overall game flow, handles playing again, and orchestrates calls to other modules.
*   `board.py`: Manages the game board's state (creation, updating) and is responsible for displaying the board in the terminal.
*   `game_logic.py`: Contains the core rules of Tic Tac Toe, including functions to check for winning conditions, detect draws, and switch players.
*   `player.py`: Handles user interaction, specifically getting and validating the player's move input.
*   `README.md`: This file, providing information about the project.

## Requirements

*   Python 3.x

## How to Run

1.  **Ensure you have Python 3 installed.**
2.  **Save the files:** Make sure all the `.py` files (`main.py`, `board.py`, `game_logic.py`, `player.py`) are in the same directory (e.g., a folder named `tic_tac_toe`).
3.  **Open your terminal or command prompt.**
4.  **Navigate to the directory** where you saved the files using the `cd` command.
    ```bash
    cd path/to/your/tic_tac_toe_folder
    ```
5.  **Run the main script:**
    ```bash
    python main.py
    ```
6.  Follow the on-screen prompts to play the game! Enter numbers 1-9 corresponding to the positions on the board.

## Gameplay

*   Player 'X' always starts.
*   Players take turns entering a number from 1 to 9 to place their mark on the corresponding empty cell.
*   The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.
*   If all cells are filled and no player has won, the game is a draw.