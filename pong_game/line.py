from turtle import Turtle
DOWN = 270

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.pendown()
        self.setheading(DOWN)
        for y in range(240, -290, -11):
            self.forward(6)
            self.penup()
            self.forward(6)
            self.pendown()
