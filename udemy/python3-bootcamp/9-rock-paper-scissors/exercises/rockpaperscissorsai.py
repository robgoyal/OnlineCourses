import random

# Print introductory messages
print("...rock...")
print("...paper...")
print("...scissors...")

# Get player 1's choice
player_choice = input("(Enter your choice): ")

# Get player 2's choice
computer_choice = random.choice(["rock", "scissors", "paper"])
print("The computer plays: {}".format(computer_choice))

# Determine winner
win_conds = (("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"))
if player_choice == computer_choice:
    msg = "Tie"
elif (player_choice, computer_choice) in win_conds:
    msg = "Player1 wins"
elif (computer_choice, player_choice) in win_conds:
    msg = "Computer wins"

# Print winner
print(msg)