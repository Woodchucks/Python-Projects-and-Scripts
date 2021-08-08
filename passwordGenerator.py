#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

list_chosen = []
for letter in range(1,nr_letters+1):
  letter_chosen = random.choice(letters)
  list_chosen.append(letter_chosen)
for symbol in range(1,nr_symbols+1):
  symbol_chosen = random.choice(symbols)
  list_chosen.append(symbol_chosen)
for number in range(1,nr_numbers+1):
  number_chosen = random.choice(numbers)
  list_chosen.append(number_chosen)

password = ""
for item in range(1,len(list_chosen)+1):
  choose_item = random.choice(list_chosen)
  print(choose_item)
  password = password + choose_item
  list_chosen.remove(choose_item)
print(password) 
