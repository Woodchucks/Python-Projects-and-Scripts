from turtle import Screen, Turtle
from random import randint
# import colorgram

guc = Turtle()
screen = Screen()

# list_of_color_tuples = []
# def create_color_table(name_of_picture, nr_of_colors):
    # colors = colorgram.extract(name_of_picture, nr_of_colors)
    # for color in colors:
      #   r = color.rgb.r
       #  g = color.rgb.g
      #   b = color.rgb.b
       #  new_color = (r, g, b)
       #  list_of_color_tuples.append(new_color)

# print(list_of_color_tuples("cologram.jpg", 10))

def rand_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r, g, b)
    return random_color

guc.speed("fastest")
guc.penup()
guc.hideturtle()
y = -200
guc.goto(-300,y)
print(guc.pos())

for _ in range(10):
    for _ in range(10):
        #col = rand_color()
        guc.dot(20, "blue")
        guc.forward(50)
    y += 50
    guc.goto(-300,y)

screen.exitonclick()
