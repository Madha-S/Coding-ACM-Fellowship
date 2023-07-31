import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input=input("Enter Rock/Paper/Scissors or Quit>> ")
    if user_input.lower() == "quit":
        break
    if user_input.lower() not in options:
        continue
       
    random_number=random.randint(0,2)
    comp_pick=options[random_number]
    print(f"Computer picked {comp_pick}")
    
    if (user_input=="rock" and comp_pick=="scissors") or (user_input=="paper" and comp_pick=="rock") or (user_input=="scissors" and comp_pick=="paper"):
        print("You Win!")
        user_wins+=1
    elif (user_input=="rock" and comp_pick=="rock") or (user_input=="paper" and comp_pick=="paper") or (user_input=="scissors" and comp_pick=="scissors"):
        print("Draw!")
    else:
        print("Computer Wins!")
        computer_wins+=1

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print("GOODBYE!")
