from tkinter import *
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"
FONT_LABEL_LANGUAGE = ("Ariel", 40, "italic")
FONT_LABEL_WORD = ("Ariel", 60, "bold")

#---------------------Read CSV File-----------------------------
def pick_random_word():
    records = pd.read_csv("data/french_words.csv")
    chosen_word = rd.choice(records.to_dict()["French"])
    canvas.itemconfigure(word, text=chosen_word)

# ---------------------User Interface---------------------------
window = Tk()
window.title("Learn French!")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_image = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_image)
canvas.create_text(400, 150, text="French", font=FONT_LABEL_LANGUAGE)
word = canvas.create_text(400, 263, text="some word", font=FONT_LABEL_WORD)
canvas.grid(row=0, column=0, columnspan=2)

wrong_icon = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_icon, highlightthickness=0, command=pick_random_word)
button_wrong.grid(row=1, column=0)
right_icon = PhotoImage(file="images/right.png")
button_right = Button(image=right_icon, highlightthickness=0, command=pick_random_word)
button_right.grid(row=1, column=1)

window.mainloop()
