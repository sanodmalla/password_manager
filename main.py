import json
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def get_details():

    website_name = website_entry.get()
    email_add = email_entry.get()
    password_detail = password_entry.get()
    new_data = {website_name: {
        "email": email_add,
        "password": password_detail
    }}

    if website_name == "" or password_detail == "":
        messagebox.showinfo(title="Oops!", message="Please fill all the details. ")
    else:
        try:
            # Load the Json file
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # creating data file and dumping new data
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update the data with new data
            data.update(new_data)
            # Write the updated data on data file.
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            clear()


def clear():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def get_password():

    #Check the website entry and Json key match
    website = (website_entry.get()).capitalize()
    with open("data.json", mode="r") as json_data:
        data = json.load(json_data)
        try:
            data[website]
        except KeyError:
            messagebox.showinfo(title="Oops!", message="This website is not saved.")
            clear()
        else:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Here's the details.", message=f"email: {email}\n password: {password}")




    #if no match, pop up msg

    #else pop up box with username and password


# ---------------------------- UI SETUP ------------------------------- #


# window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(width=700, height=500)

# image canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:")
email = Label(text="Email/Username:")
password = Label(text="Password:")

# Entries
website_entry = Entry(width=21)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.insert(0, "sanodmalla@gmail.com")
password_entry = Entry(width=21)

# Buttons
search = Button(text="Search", width=15, command=get_password)
generate = Button(text="Generate Password", width=15, command=generate_password)
add_button = Button(text="Add", width=38, command=get_details)

# Label and entry grids
website.grid(column=0, row=1)
email.grid(column=0, row=2)
password.grid(column=0, row=3)
website_entry.grid(column=1, row=1)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)
generate.grid(column=2, row=3)
search.grid(column=2, row=1)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()