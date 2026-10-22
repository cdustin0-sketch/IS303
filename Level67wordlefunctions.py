import random


def choose_word():
    """Choose and return a secret five-letter word."""
    words = [
        "CRANE", "SLATE", "BRICK", "MOUSE", "PLANT",
        "GRAPE", "SOUND", "TABLE", "CHAIR", "STONE",
        "PROUD", "FLAME", "GHOST", "CROWN", "DRINK",
        "SPEAR", "CLOUD", "TRAIN", "BEACH", "LIGHT",
        "MONEY", "QUIET", "ROUND", "SUGAR", "VOICE",
        "WHEAT", "ZEBRA", "SHARK", "TIGER", "LEMON",
        "PEACH", "OLIVE", "PIANO", "HOUSE", "BREAD",
        "CIDER", "CRISP", "BLOND", "TRACK", "SWING",
        "HEART", "PLAIN", "STORM", "FAITH", "GLOVE",
        "DRAMA", "FRESH", "GIANT", "HORSE", "IDEAL",
        "JOKER", "KNIFE", "LAUGH", "MARCH", "NOBLE",
        "OCEAN", "PRICE", "QUEST", "RADIO", "SMART",
        "THING", "UNCLE", "VAPOR", "WORLD", "YOUNG",
        "ADORE", "BONUS", "CHARM", "DAISY", "ENTRY",
        "FOCAL", "HONEY", "INPUT", "JUMPY", "LIVER",
        "MANGO", "NURSE", "ORBIT", "PATCH", "RISKY",
        "STEAM", "URBAN", "WRIST", "YOUTH", "ABIDE",
        "BOUND", "CHASE", "DOUBT", "FROST", "GRAIN",
        "INDEX", "JOINT", "KARMA", "LIMIT", "MAYOR",
        "NOVEL", "PAINT", "RATIO", "SPEND", "TRUST"]
    return random.choice(words)


def get_guess(previous_guesses):
    """Get a five-letter guess that has not been used before."""
    while True:
        guess = input("Enter a five-letter word: ").strip().upper()

        if len(guess) != 5:
            print("Your guess must contain exactly five letters.")
        elif not guess.isalpha():
            print("Please enter letters only.")
        elif guess in previous_guesses:
            print("You already guessed that word.")
        else:
            return guess


def evaluate_guess(guess, secret_word):
    """Return G, Y, or - for each letter in the guess."""
    feedback = []

    for index in range(5):
        letter = guess[index]

        if letter == secret_word[index]:
            feedback.append("G")
        elif letter in secret_word:
            feedback.append("Y")
        else:
            feedback.append("-")

    return feedback


def display_guess(guess, feedback):
    """Display the guess and its feedback."""
    print("Guess:   ", " ".join(guess))
    print("Feedback:", " ".join(feedback))


def has_won(guess, secret_word):
    """Return True if the guess matches the secret word."""
    return guess == secret_word