from tkinter import *
import pandas as pd
import random as rd
import os.path

BACKGROUND_COLOR = "#B1DDC6"
FONT_LABEL_LANGUAGE = ("Ariel", 40, "italic")
FONT_LABEL_WORD = ("Ariel", 60, "bold")

words_to_learn_file_created = os.path.exists("data/words_to_learn.csv")
if words_to_learn_file_created:
    records = pd.read_csv("data/words_to_learn.csv")
else:
    records = pd.read_csv("data/french_words.csv")
to_learn = records.to_dict(orient="records")
current_card = {}

#---------------------Read CSV File-----------------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = rd.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_image_front)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

#---------------------Flip cards--------------------------------
def flip_card():
    canvas.itemconfig(canvas_image, image=card_image_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=card_image_back)
    canvas.itemconfig(word, text=current_card['English'], fill="white")

#--------------------Remove learned word from learning list------
def remove_from_learning_list():
    global to_learn, current_card
    to_learn.remove(current_card)
    words_to_learn = pd.DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------User Interface---------------------------
window = Tk()
window.title("Learn French!")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(100, func=next_card)

card_image_front = PhotoImage(file="images/card_front.png")
card_image_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_image_front)
language = canvas.create_text(400, 150, text="", font=FONT_LABEL_LANGUAGE)
word = canvas.create_text(400, 263, text="", font=FONT_LABEL_WORD)
canvas.grid(row=0, column=0, columnspan=2)

wrong_icon = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_icon, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)
right_icon = PhotoImage(file="images/right.png")
button_right = Button(image=right_icon, highlightthickness=0, command=remove_from_learning_list)
button_right.grid(row=1, column=1)

window.mainloop()
