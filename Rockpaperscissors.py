import random
#Show the available choices
choices=["R","P","S"]
#input the available choices for the user
user_choice=input("Enter your choice (R for Rock, P for Paper, S for Scissors): ")
if user_choice not in choices:
    print("Invalid choice. Please select R, P, or S.")
else:
#Select a random choice for the computer
 computer_choice=random.choice(choices)
 print(f"Computer chose: {computer_choice}")
 #Show the winner
 if user_choice == computer_choice:
     print("The match is a tie")
 elif (user_choice == "R" and computer_choice == "S") or (user_choice == "P" and computer_choice == "R") or (user_choice == "S" and computer_choice == "P"):
     print("You are the winner")
 else:
     print("Computer wins")