import random
from art import logo
print(logo)

# Greet the user
print("Welcome to the number guessing game.")

# Give user insight about the game
print("I have a number in my mind between 1 and 100.")

# Let user choose difficulty level (guessing attempts: hard - 5, easy - 10)
level = input("Choose difficulty level. Type 'easy' or 'hard' ")
attempts = 10
if level == 'hard':
  attempts -= 5

# Choose a random number between 1 and 100
def rand_nr():
  number = random.randint(1, 100)
  return number

# loop -> Tell user how many attempts are remaining, Get guess from user
def guess_nr():
  global attempts
  print(f"You have {attempts} attempts remaining to guess the number.")
  attempts -= 1
  guess = int(input("Make a guess: "))
  return guess

# loop -> give user feedback (too high, too low, tell user to guess again)
game_over = False
number_to_be_guessed = rand_nr()
while attempts > 0 and not game_over:
  users_guess = guess_nr()
  if number_to_be_guessed < users_guess:
    print("Too high")
  elif number_to_be_guessed > users_guess:
    print("Too low.")
  # if user wins -> tell user he won and what the nr was
  elif number_to_be_guessed == users_guess:
    print(f"You got it! the answer was {users_guess}")
    game_over = True
# elif user looses -> Tell user he ran out of attempts and has lost
if attempts == 0:
  print("You've run out of guesses. Game Over.")
