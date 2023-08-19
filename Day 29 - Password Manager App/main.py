from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager by nubcoder420")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=img)
canvas.grid(row=1, column=1)

website_label = Label(text="Website:")
website_label.grid(row=2, column=0)

website_entry = Entry(width=55)
website_entry.grid(row=2, column=1, columnspan=2)

username_label = Label(text="Email/Username:")
username_label.grid(row=3, column=0)

username_entry = Entry(width=55)
username_entry.grid(row=3, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=4, column=0)

password_entry = Entry(width=36)
password_entry.grid(row=4, column=1)

generate_button = Button(text="Generate Password")
generate_button.grid(row=4, column=2)

add_button = Button(text="Add", width=47)
add_button.grid(row=5, column=1, columnspan=2)













window.mainloop()
