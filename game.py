import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
print(f"The computer chose: {computer}")
player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
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
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1


