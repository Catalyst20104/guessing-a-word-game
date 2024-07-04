# Multiplayer Word Guessing Game

This project is a multiplayer word guessing game where two players compete to guess a word. The game continues until both players guess the same word. It uses socket programming and multi-threading in Python to enable gameplay across different terminals.

## Features

- **Multiplayer Support**: Two players can connect from different terminals.
- **Socket Programming**: Facilitates communication between players over the network.
- **Multi-threading**: Handles different tasks simultaneously, ensuring smooth gameplay.

## How It Works

1. **Setup**: The server is started and waits for connections from two players.
2. **Gameplay**: Each player attempts to guess the word. They continue guessing until both players guess the same word.
3. **End Game**: The game ends when both players have guessed the same word, and the result is displayed.

## Requirements

- Python 3.x
- Socket programming module (built-in with Python)
- Threading module (built-in with Python)

## How to Run

1. **Start the Server**:
    ```bash
    python server.py
    ```
2. **Start the Players**:
    ```bash
    python player.py
    ```

Players will be prompted to enter their guesses, and the game will notify when both players have guessed the same word.
