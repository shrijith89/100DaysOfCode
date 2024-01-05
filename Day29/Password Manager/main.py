import tkinter
import pandas
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_data():
    if len(websiteInput.get()) == 0 or len(passwordField.get()) == 0:
        messagebox.showinfo(title="Empty Data", message="Fill all the fields")

    else:
        flag = messagebox.askokcancel(title="Data Added", message=f"These are the details entered: "
                                                                  f"email:{emailInput.get()}\n password:{passwordField.get()}\n"
                                                                  f"can be saved.?")

        if flag:
            with open("example.txt", 'a') as f:
                f.write(websiteInput.get() + " | " + emailInput.get() + " | " + passwordField.get())
                f.write("\n")

            websiteInput.delete(0, 'end')
            emailInput.delete(0, 'end')
            passwordField.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
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
emailInput.insert(5, "p.shrijith@test.com")
emailInput.grid(row=3, column=1, columnspan=2)

passwordField = tkinter.Entry(width=21)
passwordField.grid(row=4, column=1)

# Buttons
generateButton = tkinter.Button(text="Generate Password")
generateButton.grid(row=4, column=2)

addButton = tkinter.Button(text="Add", width=31, command=write_data)
addButton.grid(row=5, column=1, columnspan=2)

window.mainloop()
