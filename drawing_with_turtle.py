from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forwards():
    tom.forward(100)

def move_backwards():
  tom.backward(100)

def move_counter_clockwise():
  new_heading = tom.heading() - 10
  tom.setheading(new_heading)

def move_clockwise():
  new_heading = tom.heading() + 10
  tom.setheading(new_heading)

def clear_drawing():
  tom.clear()
  tom.penup()
  tom.home()
  tom.pendown()

screen.mode("logo")
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_drawing, "c")

screen.listen()

screen.exitonclick()
