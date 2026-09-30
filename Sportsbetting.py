import random

guess = 0
num_guesses = 0


print("Welcome to the Higher/Lower Game")

#Get a random number for the user to gues
solution = random.randint(1, 100)

def one_play():
    #
    while guess != solution:

        #Get and validate user input
        guess = int(input("Guess a number between 1 and 100: "))
        while (guess < 1 and guess > 100):
            guess = int(input("Invalid number. Please try again: "))

        num_guesses += 1
        #Determine the result
        if guess > solution:
            print("Lower")
        elif guess < solution:
            print("Higher")
        elif guess == solution:
            print("You got it right!")

    #loop

    print(f"It took you {num_guesses} guesses")

