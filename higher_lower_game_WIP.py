  # {
  #       'name': 'Cristiano Ronaldo',
  #       'follower_count': 215,
  #       'description': 'Footballer',
  #       'country': 'Portugal'
  #   },
from random import randint
from game_data import data
# import arts and print game logo
from art import logo
print(logo)
# randomly assign A and B from data, delete A and B from data set

def rand_indx():
  return randint(0, len(data))

def assign_person(indx):
  data_item = data[indx]
  _name = data_item["name"]
  _descr = data_item["description"]
  _country = data_item["country"]
  return f"{_name}, a {_descr}, from {_country}."
# create compare function and compare A and B's follower_count keys, return highest Value
def most_followers(data_indx_A, data_indx_B):
  followers_A = data[data_indx_A]["follower_count"]
  followers_B = data[data_indx_B]["follower_count"]
  if followers_A > followers_B:
    return "A"
  elif followers_B > followers_A:
    return "B"
  else:
    return ""

score = 0  
def right_guess(guess, most_followers_func):
  global game_over
  if guess == most_followers_func:
    global score
    score = score + 1
    print(f"You're right! Current score: {score}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    game_over = True

game_over = False
def game():
  rand_indx_A = rand_indx()
  rand_indx_B = rand_indx()
  A = assign_person(rand_indx_A)
  B = assign_person(rand_indx_B)
  print(f"Compare A: {A}.")
  # print(vs)
  print(f"Against B: {B}.")
  while not game_over:
    guess = input("Who has more followers? Type 'A' or 'B'")
    right_guess(guess, most_followers(rand_indx_A,rand_indx_B))

game()



# Assign A to highest value
# print "vs" art
#Who has more followers? if right answer
  # score ++
  # print "You're right! Curen score ...."
# else 
  # print "Sorry, that's wrong. Final score: ..."
