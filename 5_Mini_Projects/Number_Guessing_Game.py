import random

range=input("Enter a number>> ")
if range.isdigit():
    range=int(range)
    if range<=0:
        print("Please! Enter a number larger than zero.")
        quit()
else:
    print("Please enter a number next time.")

random_number=random.randint(0, range)

guesses=0
while True:
    guesses+=1
    user_guess=input("Make a guess>> ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please enter a number.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess>random_number:
        print("Try guessing lower than this!")
    else:
        print("Try guessing a larger number!")
print(f"You got it in {guesses}th guess.")