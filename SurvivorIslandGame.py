print("Welcome to Survival Island.")
print("Your mission is to find the the Princess missing crown!.") 

decision = (input("You came to a crossroad - which way do you want to go (left, right)?\n")).lower()
if decision == "left":
  activity = (input("Watch out! There's a small lake ahead! You want to swim or wait for a boat (wait, swim)?\n")).lower()
  if activity == "wait":
    door = (input("You sucessfully crossed the lake. Now 3 doors appeared in front of you: a red one, a blue one and a yellow one. Which one do you choose (red, blue, yellow)?\n")).lower()
    if door == "yellow":
      print("congratulations. You win!")
    elif door == "blue":
      print("You got eaten by a crocodile. Game over.")
    elif door == "red":
      print("You fell into a hole. Game over.")
    else:
      print("Game Over.")
  else:
    print("You got eaten by a wolf. Game Over.")
else:
  print("You got hit by a bird. Game over.")
