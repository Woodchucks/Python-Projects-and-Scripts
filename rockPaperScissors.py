#first draft, to be continued with number values
#right now does not prevent from error if user inserts a different name from paper, scissors, rock

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock - Scissors - Paper Tournament.")
print("Let the better win!!!")

possible_figures = [rock, paper, scissors]
possible_figures_items_as_strings = ["rock", "paper", "scissors"]
rand_nr = random.randint(1,3)

#figure which the computer plays against you
figure_computer_plays = possible_figures[rand_nr-1]

figure = (input("Which figure do you want to play? /Choose eighter rock, scissors or paper/\n")).lower()

#changing figure chosen into visual
if figure == "rock":
  chosen_figure = possible_figures[0]
elif figure == "paper":
  chosen_figure = possible_figures[1]
elif figure == "scissors":
  chosen_figure = possible_figures[2]

if figure == "paper" or figure == "rock" or figure == "scissors":
  print(figure)
else:
  print("Spelling error, play again.")
print(chosen_figure)
print("Computer chose:")
print(figure_computer_plays)

#determining the winner
if (chosen_figure == figure_computer_plays):
  print("Draw. Play again.")
elif (figure == "rock" and possible_figures_items_as_strings[rand_nr-1] == "paper") or (figure == "scissors" and possible_figures_items_as_strings[rand_nr-1] == "rock") or (figure == "paper" and possible_figures_items_as_strings[rand_nr-1] == "scissors"):
  print("You loose.")
elif (figure == "rock" and possible_figures_items_as_strings[rand_nr-1] == "scissors") or (figure == "scissors" and possible_figures_items_as_strings[rand_nr-1] == "paper") or (figure == "paper" and possible_figures_items_as_strings[rand_nr-1] == "rock"):
  print("You win.")
