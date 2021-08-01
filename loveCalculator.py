print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

#count occurence of letters in 't r u e l o v e'
t = name1_lower.count("t") + name2_lower.count("t")
r = name1_lower.count("r") + name2_lower.count("r")
u = name1_lower.count("u") + name2_lower.count("u")
e = name1_lower.count("e") + name2_lower.count("e")
l = name1_lower.count("l") + name2_lower.count("l")
o = name1_lower.count("o") + name2_lower.count("o")
v = name1_lower.count("v") + name2_lower.count("v")

per1 = t+r+u+e
per2 = l+o+v+e

percentage = int(str(per1) + str(per2))

print(percentage)

if percentage < 10 or percentage > 90:
  print(f"Your score is {percentage}, you go together like coke and mentos.")
elif percentage >= 40 and percentage <= 50:
  print(f"Your score is {percentage}, you are alright together.")
else:
  print(f"Your score is {percentage}.")
