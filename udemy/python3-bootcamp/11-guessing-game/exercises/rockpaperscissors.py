import random

wins = {"computer": 0, "player": 0}

print(f"Scores: computer: {wins['computer']}, player: {wins['player']}")
while wins["computer"] != 3 and wins["player"] != 3:

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
        msg = "This round is a tie!"
    elif (player_choice, computer_choice) in win_conds:
        msg = "Player wins this round!"
        wins["player"] += 1
    elif (computer_choice, player_choice) in win_conds:
        msg = "Computer wins this round!"
        wins["computer"] += 1

    # Print winner
    print(msg, end="\n\n")
    print(f"Scores: computer: {wins['computer']}, player: {wins['player']}")

if wins["computer"] == 3:
    print("The computer has won best out of 5!")
else:
    print("The player has won best out of 5!")
