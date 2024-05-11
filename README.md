# Quantum_Computing

This Python script implements a version of the Mastermind game with an optimization strategy to minimize the number of attempts needed to guess the secret code.

## Game Overview

Mastermind is a code-breaking game where one player (the codemaker) creates a secret code consisting of a sequence of colored pegs, and the other player (the codebreaker) attempts to guess the code. After each guess, the codemaker provides feedback to indicate the correctness of the guess.

## Game Logic

- **Secret Code Generation**: The game generates a random secret code consisting of a sequence of colors. Each color can be chosen from a predefined set of colors.

- **Guess Evaluation**: After each guess, the game evaluates the guess against the secret code. The evaluation provides feedback in the form of two numbers:
    - Number of correct colors in the correct positions (black pegs)
    - Number of correct colors in incorrect positions (white pegs)

- **Optimization Strategy**: The script implements an optimization strategy based on Donald Knuth's algorithm to minimize the number of attempts needed to guess the secret code. The algorithm selects the most efficient guess based on the current set of possible codes and the feedback received from previous guesses.

3. **Run the Script**: Run the Python script using the following command:

    ```bash
    python game.py
    ```

## Parameters

- `NUM_TRIES`: Number of attempts allowed to guess the secret code.
- `CODE_LENGTH`: Length of the secret code.
- `NUM_COLORS`: Number of colors available for the code.

