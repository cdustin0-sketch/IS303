import random


def get_player_choice():
    while True:
        choice = input("Enter rock, paper, or scissors: ")
        choice = choice.lower()

        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Not a valid option, please try again.")


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"

    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "scissors" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        return "win"

    else:
        return "loss"


rounds = int(input("How many rounds would you like to play? "))

while rounds <= 0 or rounds % 2 == 0:
    print("The number must be a positive odd number.")
    rounds = int(input("Please try again: "))

print("Rounds:", rounds)

player_wins = 0
computer_wins = 0
completed_rounds = 0

while completed_rounds < rounds:
    player_choice = get_player_choice()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("The computer chose", computer_choice)

    result = determine_winner(player_choice, computer_choice)

    if result == "tie":
        print("Tie! Play again.")
    elif result == "win":
        print("You won!")
        player_wins += 1
        completed_rounds += 1
    else:
        print("You lost!")
        computer_wins += 1
        completed_rounds += 1

print("-------------------------------------------")
print(f"Score - You: {player_wins} | Computer: {computer_wins}")

if player_wins > computer_wins:
    print("You win!!!")
else:
    print("Computer wins!!!")

print("Thanks for playing!")