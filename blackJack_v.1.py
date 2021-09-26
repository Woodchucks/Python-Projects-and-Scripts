# Show blackjack logo
from art import logo
import random
import os

print(logo)

# Ask user if he wants o play a game of Blackjack
def play_game():
  play_game = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no ")
  return play_game

def clear():
    os.system('clear')

def choose_card(cards):
  """Chose card randomely from cards list"""
  card = random.choice(cards)
  return card

def add_card(cards, card):
  """As arguments pass in list of cards and card you want to add to card list"""
  cards.append(card)

def print_cards(cards):
  """Print all cards in list"""
  print(cards)

def add_score(score, card):
  """Add card to score variable"""
  return score + card

def over_21(user_score, comp_score):
  if user_score > 21:
    print("You went over, you lose.")
  elif comp_score > 21:
    print("Opponent went over, you win.")
  else:
    return ""

def compare_scores(user_score, comp_score):
  if user_score == comp_score:
    print("Draw.")
  elif user_score > comp_score:
    print(f"You won with score {user_score}.")
  elif comp_score > user_score:
    print(f"You lost, computer won.")

#Create list of possible cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_game = play_game()
while play_game == 'y':
  #Choose possible cards for computer
  comp_card_1, comp_card_2, comp_card_3 = random.sample(cards, 3)
  comp_cards = []
  comp_card_1 = choose_card(cards)
  comp_card_2 = choose_card(cards)
  add_card(comp_cards, comp_card_1)
  add_card(comp_cards, comp_card_2)
  comp_score = 0
  comp_score = add_score(comp_score, comp_card_1)
  comp_score = add_score(comp_score, comp_card_2)

  # Add user's cards to list
  user_cards = []
  user_card_1 = choose_card(cards)
  user_card_2 = choose_card(cards)
  add_card(user_cards, user_card_1)
  add_card(user_cards, user_card_2)
  user_score = 0
  user_score = add_score(user_score, user_card_1)
  user_score = add_score(user_score, user_card_2)

  #Show computer's and user's first cards in console
  print("Your cards: ")
  print_cards(user_cards)
  print("current score: ")
  print(user_score)
  print(f"Computer's first card is {comp_card_1}")

  anoth_card = input("Type 'y' to get another card, type 'n' to pass. ")
  while anoth_card == 'y':
    user_card = choose_card(cards)
    add_card(user_cards, user_card)
    user_score = add_score(user_score, user_card)
    comp_card = choose_card(cards)
    add_card(comp_cards, comp_card)
    comp_score = add_score(comp_score, comp_card)
    print("Your cards: ")
    print_cards(user_cards)
    print("current score: ")
    print(user_score)
    print(f"Computer's first card {comp_card_1}")
    compare = over_21(user_score, comp_score)
    if user_score > 21 or comp_score >21:
      anoth_card = 'n'
    else:
      anoth_card = input("Type 'y' to get another card, type 'n' to pass. ")
  if user_score > 21 or comp_score > 21:
    print("")
  else:
    print(f"Your final hand: ")
    print_cards(user_cards)
    print("Your final score: ")
    print(user_score)
    print("Computer's final hand: ")
    print_cards(comp_cards)
    print("Computer's final score: ")
    print(comp_score)
    compare_2 = compare_scores(user_score, comp_score)
  play_game = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no ")
  clear()
print("See you soon! Have a nice day.")
