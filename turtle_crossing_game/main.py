from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #detct turtle's collision with top edge, reset turtle's position
    if player.ycor() > 280:
        player.reset_position()
        car_manager.speed_up_car()
        score_board.level_up()

    #detect turtle's collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.print_game_over()

screen.exitonclick()
