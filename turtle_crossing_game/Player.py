from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -280)
        self.shape("turtle")
        self.color("black")
        self.setheading(90)

    def move(self):
        self.forward(10)

    def reset_position(self):
        self.hideturtle()
        self.goto(0, -280)
        self.showturtle()
