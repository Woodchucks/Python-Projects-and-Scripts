import random
from turtle import Turtle, Screen
from random import choice

is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["yellow", "red", "green", "blue", "orange", "violet"]
turtles = []

def create_turtle():
    new_turtle = Turtle(shape="turtle")
    color = choice(colors)
    new_turtle.color(color)
    colors.remove(color)
    new_turtle.penup()
    turtles.append(new_turtle)
    return new_turtle

x= -230
y= -100

for _ in range(6):
    turtle_instance = create_turtle()
    turtle_instance.goto(x, y)
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
