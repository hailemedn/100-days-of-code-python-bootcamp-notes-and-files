from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# places a label on the screen
my_label.pack()

# ways to change the content of label
my_label["text"] = "I am a new label"
my_label.config(text="New Text")

# you can't mix grid and pack
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=5, pady=3)


def button_clicked():
    new_text = input_box.get()
    my_label.config(text=new_text)


# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input_box = Entry()
# input_box.pack()
input_box.grid(column=3, row=2)
input_box.get()

window.mainloop()
