from Level67wordlefunctions import (
    choose_word,
    get_guess,
    evaluate_guess,
    display_guess,
    has_won,
)

def play_game():
    print("\nWelcome to Mystery Wordle!")
    print("Guess the five-letter word.")
    print("G = correct letter and position")
    print("Y = correct letter, wrong position")
    print("- = letter is not in the word")

    secret_word = choose_word()
    previous_guesses = []
    maximum_attempts = 6

    for attempt in range(1, maximum_attempts + 1):
        print(f"\nAttempt {attempt} of {maximum_attempts}")

        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)

        feedback = evaluate_guess(guess, secret_word)
        display_guess(guess, feedback)

        if has_won(guess, secret_word):
            print("Congratulations! You solved the puzzle.")
            return

    print(f"\nYou're out of attempts. The secret word was {secret_word}.")


def main():
    while True:
        play_game()

        play_again = input("\nWould you like to play again? ").strip().lower()

        if play_again != "yes" and play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()