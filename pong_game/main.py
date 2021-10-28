from turtle import Screen
from paddle import Paddle
from line import Line
from score import Score
from ball import Ball
import time

STARTING_POSITION_1 = (-350, 0)
STARTING_POSITION_2 = (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("LET'S PONG BABY")
screen.tracer(0)

score_player_1 = Score()
score_player_2 = Score()
paddle_1 = Paddle(STARTING_POSITION_1)
paddle_2 = Paddle(STARTING_POSITION_2)
line = Line()
ball = Ball()

screen.listen()
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.current_speed)
    screen.update()
    ball.move()

    # detect ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect ball collision with paddle
    if ball.xcor() > 320 and ball.distance(paddle_2) < 50 or ball.xcor() < -320 and ball.distance(paddle_1) < 50:
        ball.bounce_x()
        ball.current_speed /= 2

    #detect when ball goes off of bounds
    if ball.xcor() > 390:
        score_player_1.get_point()
        ball.reset_position()

    if ball.xcor() < -390:
        score_player_2.get_point()
        ball.reset_position()

    score_player_1.update_score(score_player_2.score)

screen.exitonclick()
