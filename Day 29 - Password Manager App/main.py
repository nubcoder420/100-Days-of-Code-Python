from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

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
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if website == "" or username == "":
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
                #Update old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ------------------------- FIND PASSWORD ---------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title="Match Found", message=f"Website: {website}\n"
                                                             f"Username/Email: {data[website]['email']}\n"
                                                             f"Password: {data[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No matches for '{website}' found")


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

website_entry = Entry(width=36)
website_entry.grid(row=2, column=1)
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

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=2, column=2)

window.mainloop()
