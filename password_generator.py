from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input_box.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input_box.get()
    email = email_username_box.get()
    password = password_input_box.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Do you want to save the following data? \nEmail: {email}\nPassword: {password}")

        if is_ok:
            file = open("data.txt", "a")
            file.write(f"{website} | {email} | {password} \n")
            website_input_box.delete(0, 'end')
            password_input_box.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_email_username = Label(text="Email/ Username:")
label_email_username.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

website_input_box = Entry(width=35)
website_input_box.grid(row=1, column=1, columnspan=2)
website_input_box.focus()
email_username_box = Entry(width=35)
email_username_box.grid(row=2, column=1, columnspan=2)
email_username_box.insert(0, "sandra@email.com")
password_input_box = Entry(width=21)
password_input_box.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
