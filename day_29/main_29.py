from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate():
    nr_letters = random.randint(8, 16)
    nr_symbols = random.randint(4, 8)
    nr_numbers = random.randint(4, 8)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    return password


def generate_password():
    password = generate()
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if password == "" or username == "" or website == "":
        messagebox.showinfo(title="Error", message="Website, username or password details are empty.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n Email: {username}"
                                                          f"\n Password: {password}\n Is it ok to save?")

    if not is_ok:
        return

    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }
    try:
        with open("password_manager.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
    except FileNotFoundError:
        with open("password_manager.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        with open("password_manager.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()

    if website == "":
        messagebox.showinfo(title="Error", message="You just search for empty website")
        return

    try:
        with open("password_manager.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There is no websites stored yet.")
    else:
        if website in data.keys():
            messagebox.showinfo(title=website, message=f"username: {data[website]['username']}\n"
                                                       f"password: {data[website]['password']}")
        else:
            messagebox.showinfo(title=website, message=f"There is no such website as {website} stored yet.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()

website_button = Button(text="Search", width=15, command=search)
website_button.grid(row=1, column=2)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "example@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()