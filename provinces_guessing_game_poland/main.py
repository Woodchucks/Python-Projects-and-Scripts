import turtle
import pandas

data = pandas.read_csv("16_provinces.csv")
all_provinces = data.province.to_list()
score = 0
attempts = 0

map = "poland_contour_map.gif"
screen = turtle.Screen()
screen.addshape(map)
screen.title("Poland Provinces Game")

turtle.shape(map)

# Get provinces coordinates
# def show_coor(x, y):
#     print(x, y)
# screen.onscreenclick(show_coor)
# screen.mainloop()

guessed_provinces = []

while len(guessed_provinces) <= 16 and attempts <= 20:
    attempts += 1
    answer_province = screen.textinput(title=f"{score}/20 provinces", prompt="Name a Polish province").title()

    if answer_province == "Exit":
        provinces_to_learn = []
        for province in all_provinces:
            if province not in guessed_provinces:
                provinces_to_learn.append(province)
        new_data = pandas.DataFrame(provinces_to_learn)
        new_data.to_csv("provinces_to_learn.csv")
        break
    if answer_province in all_provinces:
        guessed_provinces.append(answer_province)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.province == answer_province]
        t.goto(int(province_data.x), int(province_data.y))
        t.write(answer_province)
