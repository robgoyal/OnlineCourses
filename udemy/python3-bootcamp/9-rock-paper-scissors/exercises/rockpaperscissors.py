# Print introductory messages
print("...rock...")
print("...paper...")
print("...scissors...")

# Get player 1's choice
p1_choice = input("(enter Player 1's choice): ")

# Get player 2's choice
p2_choice = input("(enter Player 2's choice): ")

# Determine winner
win_conds = (("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"))
if p1_choice == p2_choice:
    msg = "Tie"
elif (p1_choice, p2_choice) in win_conds:
    msg = "player1 wins"
elif (p2_choice, p1_choice) in win_conds:
    msg = "player2 wins"

# Print closing messages
print("SHOOT!")
print(msg)