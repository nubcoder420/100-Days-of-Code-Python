from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    pass_word = "".join(password_list)
    password_entry.insert(0, pass_word)
    pyperclip.copy(pass_word)

    # print(f"Your password is: {pass_word}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askyesno(title="Proceed?",
                                    message=f"Website: {website}\nEmail/Username: {username}\nPassword: {password}")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager by nubcoder420")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=img)
canvas.grid(row=1, column=1)

website_label = Label(text="Website:")
website_label.grid(row=2, column=0)

website_entry = Entry(width=55)
website_entry.grid(row=2, column=1, columnspan=2)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=3, column=0)

username_entry = Entry(width=55)
username_entry.grid(row=3, column=1, columnspan=2)
username_entry.insert(0, "username@email.com")

password_label = Label(text="Password:")
password_label.grid(row=4, column=0)

password_entry = Entry(width=36)
password_entry.grid(row=4, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=2)

add_button = Button(text="Add", width=47, command=save)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
