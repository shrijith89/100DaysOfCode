import tkinter
from tkinter import *
from tkinter import messagebox
import password_generator
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def display_password():
    passwordField.insert(tkinter.END, password_generator.password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_data():
    website = websiteInput.get()
    email = emailInput.get()
    password = passwordField.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(websiteInput.get()) == 0 or len(passwordField.get()) == 0:
        messagebox.showinfo(title="Empty Data", message="Fill all the fields")
    else:
        flag = messagebox.askokcancel(title="Data Added", message=f"These are the details entered: "
                                                                  f"email:{emailInput.get()}\n password:{passwordField.get()}\n"
                                                                  f"can be saved.?")
        if flag:
            with open("example.json", 'r') as f:
                # Writing_data
                # json.dump(new_data, f, indent=4)
                # reading_data
                # data = json.load(f)
                # print(data)

                # update_data
                data = json.load(f)
                data.update(new_data)

            with open("example.json", 'w') as f:
                json.dump(data, f, indent=4)
                websiteInput.delete(0, 'end')
                emailInput.delete(0, 'end')
                passwordField.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager 2")
window.config(padx=50, pady=50)

logo_png = tkinter.PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=1, column=1)

# Labels
websiteLabel = tkinter.Label(text="Website:")
websiteLabel.grid(row=2, column=0)

emailUsername = tkinter.Label(text="Email/Username:")
emailUsername.grid(row=3, column=0)

passwordText = tkinter.Label(text="Password:")
passwordText.grid(row=4, column=0)

# Inputs
websiteInput = tkinter.Entry(width=35)
websiteInput.focus()
websiteInput.grid(row=2, column=1, columnspan=2)

emailInput = tkinter.Entry(width=35)
emailInput.insert(0, "p.shrijith@test.com")
emailInput.grid(row=3, column=1, columnspan=2)

passwordField = tkinter.Entry(width=21)
passwordField.grid(row=4, column=1)

# Buttons
generateButton = tkinter.Button(text="Generate Password", command=display_password)
generateButton.grid(row=4, column=2)

addButton = tkinter.Button(text="Add", width=31, command=write_data)
addButton.grid(row=5, column=1, columnspan=2)

window.mainloop()
