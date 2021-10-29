from turtle import Turtle
from random import randint

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.CAR_SPEED = 5

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.color(randint(0, 255), randint(0, 255), randint(0, 255))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(280, randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.CAR_SPEED)

    def speed_up_car(self):
        self.CAR_SPEED += 1
        for car in self.all_cars:
            car.backward(self.CAR_SPEED)
