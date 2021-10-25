from turtle import Turtle

FONT = ('Times New Roman', 15, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, 'center', FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, 'center', FONT)

    def eat_food(self):
        self.score += 1
        self.clear()
        self.update_score()
