import tkinter
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_png = tkinter.PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=1, column=1)

websiteLabel = tkinter.Label(text="Website:")
websiteLabel.grid(row=2, column=0)

websiteInput = tkinter.Entry(width=35)
websiteInput.grid(row=2, column=1, columnspan=2, padx=20)

emailUsername = tkinter.Label(text="Email/Username:")
emailUsername.grid(row=3, column=0, pady=5)

emailInput = tkinter.Entry(width=35)
emailInput.grid(row=3, column=1, columnspan=2, padx=20)

passwordText = tkinter.Label(text="Password:")
passwordText.grid(row=4, column=0, pady=5)

passwordField = tkinter.Entry(width=21)
passwordField.grid(row=4, column=1, padx=0)

generateButton = tkinter.Button(text="Generate Password")
generateButton.grid(row=4, column=2)

window.mainloop()
