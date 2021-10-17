from turtle import Screen, Turtle
from random import randint, choice

turtle_gucio = Turtle()
screen = Screen()

# for _ in range(4):
    # turtle_gucio.forward(100)
    # turtle_gucio.right(90)

# for _ in range(20):
    # turtle_gucio.pendown()
    # turtle_gucio.forward(5)
    # turtle_gucio.penup()
    # turtle_gucio.forward(5)

screen.colormode(255)

# edge = 4
# for _ in range(4, 10):
    # turtle_gucio.pencolor(randint(0,255),randint(0,255),randint(0,255))
    # for _ in range(edge):
      #   turtle_gucio.right(360/edge)
       #  turtle_gucio.forward(100)
   #  edge += 1


# turtle_gucio.pensize(15)
# turtle_gucio.speed("fastest")
# for _ in range(100):
  #   turtle_gucio.color(randint(0,255),randint(0,255),randint(0,255))
   #  turtle_gucio.setheading(choice(directions))
    # turtle_gucio.forward(30)

def rand_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r, g, b)
    return random_color

turtle_gucio.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        turtle_gucio.color(rand_color())
        turtle_gucio.circle(100)
        turtle_gucio.right(size_of_gap)

draw_spirograph(6)
screen.exitonclick()
