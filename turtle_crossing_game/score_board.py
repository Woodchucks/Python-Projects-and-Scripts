from turtle import Turtle

FONT = ('Times New Roman', 15, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-250, 260)
        self.level_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, 'center', FONT)

    def print_game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, 'center', FONT)
