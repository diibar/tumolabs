# Dice Rolling Game

## Project Description

This is a simple Python dice game for two six-sided dice. The program rolls two dice and determines whether the player wins, loses, or continues playing based on the sum of the dice.

## Game Rules

The game starts by rolling two dice.

- **Win:** If the sum is 7 or 11, the player wins immediately.
- **Lose:** If the sum is 2, 3, or 12, the player loses immediately.
- **Continue:** For any other sum, that sum becomes the player's goal number.

The player keeps rolling the dice:
- If the player rolls the goal number again, they win.
- If the player rolls 7, they lose.
- Otherwise, the game continues.

## Requirements

- Python 3.x

No external libraries are required. The project uses Python's built-in `random` module.

## How to Run

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python station_proj2.py
```

If you are using Google Colab, you can also upload and run the notebook `station_proj2.ipynb`.

## Technologies Used

- Python
- Random module

## Author

Created as part of a TUMO Labs mini-project.
