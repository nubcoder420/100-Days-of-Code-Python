from tkinter import *

WIDTH = 500
HEIGHT = 500

#window
window = Tk()
window.title("nubcoder420")
window.minsize(width=WIDTH, height=HEIGHT)

#label
my_label = Label(text="My Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label.config(text="New Label")

#button

def button_clicked():

    new_text = user_input.get()
    my_label.config(text=new_text)
    print("I got clicked.")


my_button = Button(text="Click Me", command=button_clicked)
my_button.pack()


#entry

user_input = Entry(width=20)
user_input.pack()
user_input.get()








window.mainloop()
