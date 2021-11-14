from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def miles_to_km():
    km = round(int(input.get()) * 1.61)
    label_3["text"] = km

input = Entry(width=30)
input.grid(column=1, row=0)
input.focus()

label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

label_2 = Label(text="Is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text="0")
label_3.grid(column=1, row=1)

label_4 = Label(text="Km")
label_4.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
