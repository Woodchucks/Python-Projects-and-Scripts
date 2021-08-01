import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_nr = random.randint(0,len(names)-1)
person_to_pay = names[random_nr]

print(f"{person_to_pay} is going to buy the meal today!")
