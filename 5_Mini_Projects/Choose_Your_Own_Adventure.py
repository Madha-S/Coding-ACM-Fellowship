name = str(input("Enter your good name>> "))
print(f"Welcome {name} to this adventure!")

while True:
  answer=input("You are on a dead road, it has come to an end and you can turn lft or right. Which way would you like to go? ")
  if answer.lower() == "left":
    while True:
        answer=input("You come to a river, you can walk around it or swim across it. What would you choose? ")
        if answer.lower() == "swim":
          print("You swam across and was eaten by an alligator.\nYou lost the game!")
          break
    break
        elif answer.lower() == "walk":
          print("You walked for many miles nad reached your destiny.\nYou Won!")
        break
    break
        else:
          print("Not a valid option. Try again!")
          continue
  elif answer.lower() == "right":
    while True:
        answer=input("You come to a bridge, it looks wobbly, do you want to cross it or head back?(cross/back) ")
        if answer.lower() == "cross":
          answer=input("You cross the bridge and met a stranger. Do you wish to talk or not?(yes/no) ")
          if answer.lower() == "yes":
            print("You talked to the stranger and he giftef you gold.\nYou Won!")
            break
        break
          elif answer.lower() == "no":
            print("The stranger was offended and you've lost the game.")
            break
        break
        elif answer.lower() == "back":
          print("Alas!You went back without trying and lost the game. Better luck next time.")
          break
    break
        else:
          print("Not a valid option. Try Again!")
          continue
  else:
    print("Not a valid turn. Try Again!")
    continue
