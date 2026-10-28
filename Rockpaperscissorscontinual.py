import random
#Show the available choices
choices=["R","P","S"]
user_score=0
computer_score=0
while True:
    user_choice=input("Enter your choice (R for Rock, P for Paper, S for Scissors) or Q to quit: ").upper()
if user_choice not in choices:
    print ("Invalid choice. Please try again.")
#Determine the winner
if user_choice==computer_choice:
    print("It's a tie") 
elif (user_choice=="R" and computer_choice=="S") or (user_choice=="P" and computer_choice=="R") or (user_choice=="S" and computer_choice=="P"):
    print("You win")
    user_score+=1 
else:
    print("Computer wins")
    computer_score+=1
#Ask the user if they want to play again
play_again=input("Do you want to play again? (Yes or No): ").upper()  
if play_again=="Yes":
    print("Thanks for playing.Final score is:")        