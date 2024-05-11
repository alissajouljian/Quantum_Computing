import random

def initial_guess():
    return [random.choice(range(NUM_COLORS)) for _ in range(CODE_LENGTH)]

def evaluate(secret_code, guess):
    correct_positions = sum(1 for i in range(CODE_LENGTH) if guess[i] == secret_code[i])
    correct_colors = sum(min(secret_code.count(color), guess.count(color)) for color in set(guess))
    return correct_positions, correct_colors - correct_positions

def update(all_possible_codes, guess, result):
    return [code for code in all_possible_codes if evaluate(code, guess) == result]

def optimize(all_possible_codes):
    min_worst_case = float('inf')
    best_guess = None
    for guess in all_possible_codes:
        worst_case = max(sum(1 for code in all_possible_codes if evaluate(code, guess) != result) for result in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0)])
        if worst_case < min_worst_case:
            min_worst_case = worst_case
            best_guess = guess
    return best_guess

def start(NUM_TRIES,CODE_LENGTH, NUM_COLORS):
    secret_code = initial_guess()
    print("Secret Code was:", secret_code)

    all_possible_codes = [[i, j, k] for i in range(NUM_COLORS) for j in range(NUM_COLORS) for k in range(NUM_COLORS)]

    for attempt in range(1, NUM_TRIES + 1):
        guess = optimize(all_possible_codes)
        print("Attempt", attempt, ":", guess)

        correct_positions, correct_colors = evaluate(secret_code, guess)
        print("Correct Positions:", correct_positions)
        print("Correct Colors:", correct_colors)

        if correct_positions == CODE_LENGTH:
            print("Congratulations! you guesed it in ", attempt, "attempts.")
            return

        all_possible_codes = update(all_possible_codes, guess, (correct_positions, correct_colors))

    print("Ran out of attempts. The code was:", secret_code)

if __name__ == "__main__":
    NUM_TRIES = 20
    CODE_LENGTH = 3
    NUM_COLORS = 6
    start(NUM_TRIES,CODE_LENGTH, NUM_COLORS )
