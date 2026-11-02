import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
print(f"The computer chose: {computer}")


player = input("Enter your choice (rock, paper, scissors): ").lower().strip()
print(f"You chose: {player}")

beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

if player == computer:
    print("Draw!")
elif beats[player] == computer:
    print("You win!")
else:
    print("You lose!")