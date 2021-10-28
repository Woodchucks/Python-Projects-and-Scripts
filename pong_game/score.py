from turtle import Turtle
FONT = ('Times New Roman', 30, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 255)
        self.score = 0

    def update_score(self, score_player_2):
        self.clear()
        self.write(f"{self.score} : {score_player_2}", False, 'center', FONT)

    def get_point(self):
        self.score += 1
