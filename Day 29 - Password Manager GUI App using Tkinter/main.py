
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list += [random.choice(numbers) for num in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     password += char

    # print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                # reads from json file and present it as a dictionary
                data = json.load(file)
                # updating old data with new data

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        # except json.decoder.JSONDecodeError:
        #     with open("data.json", "w") as file:
        #         json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- SEARCH ---------------------------------#


def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data was Found")
    # except json.decoder.JSONDecodeError:
    #     messagebox.showinfo(title="Error", message="No Data was Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=2, sticky="w")

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_input = Entry(width=24)
website_input.grid(row=1, column=1, columnspan=2, sticky="w")
website_input.focus()
email_input = Entry(width=43)
email_input.grid(row=2, column=1, columnspan=2, sticky="w")
email_input.insert(0, "hailemedin@gmail.com")
password_input = Entry(width=24)
password_input.grid(row=3, column=1, sticky="w")

# Buttons
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password, width=15)
generate_password_button.grid(row=3, column=2, sticky="w")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
