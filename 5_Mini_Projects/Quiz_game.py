print("Welcome to my computer qyiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score=0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print(f"You got {score} correct answers.")
if score==4:
    print("Excellent!")
elif score==3:
    print("Good!")
elif score==2:
    print("Keep it up!")
elif score==1:
    print("Needs to improve!")
else:
    print("Oh No, You've lost the quiz!")