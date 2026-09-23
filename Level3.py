#Level 3 creating a random generator game
#Create a random generator

import random

play_again = "y" 

while play_again.lower() == "y":

    secret_number = random.randint(1, 100)

    # Now create the guessing system

    guesses = 0

    guess = int(input("Enter your guess? "))

    
    while guess < 1 or guess > 100:
        guess = int(input("Please enter a number between 1 and 100:  "))

    guesses += 1
    #loop to tell them guesses
    while guess != secret_number:
        if guess < secret_number:
            print("Higher!")
        else:
            print("Lower!")
        
        guess = int(input("Enter your guess: "))
        while guess < 1 or guess > 100:
            guess = int(input("Please enter a number between 1 and 100: "))
        guesses += 1

    #Now once they guess the correct number they get a response
    print("Correct!")
    print("You got it in " + str(guesses) + " guesses! ")

    if guesses <= 3:
        print("Amazing")

    elif guesses <= 5:
        print("Impressive!")

    elif guesses <= 7:
        print("Good Job!")

    elif guesses <=9:
        print("Took a little longer, but you got there!")

    elif guesses >= 10:
        print("You need to lock in!!!")

    play_again = input("Would you like to play again? (Y/N): ")

#have the whole thing looped so they can play again if they want



