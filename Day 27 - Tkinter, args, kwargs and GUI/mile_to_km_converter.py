from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)


def convert_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.6)
    km_result_label.config(text=km)


# input
miles_input = Entry(width=7)
miles_input.grid(column=0, row=0)

# miles label
miles_label = Label(text="Miles")
miles_label.config(pady=10, padx=10)
miles_label.grid(column=1, row=0)

# km display
km_result_label = Label(text="0")
km_result_label.grid(column=0, row=1)

# km label
km_label = Label(text="km")
km_label.grid(column=1, row=1)

# calculate button
button = Button(text="Calculate", command=convert_to_km)
button.config(padx=12, pady=5)
button.grid(column=0, row=2)


window.mainloop()
