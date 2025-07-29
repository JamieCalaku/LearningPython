# Exercise 1 from lesson 29
# Rock/Paper/Scissors Game

import random

options = ("rock", "paper", "scissors")
playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, or scissors): ")

    print()
    print()
    print(f"Player: {player}")
    print(f"Computer: {computer}")


    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    print()
    print()

    if not input("Do you want to play again? (y/n): ").lower() == "y":
        playing = False

print("Thanks for playing")