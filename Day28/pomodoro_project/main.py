import tkinter
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(pady=50)
window.minsize(width=400, height=300)

#label
timer_label = tkinter.Label(text="Timer", font=("Arial", 32, "normal"), highlightcolor=RED)
timer_label.place(x=50, y=50)
timer_label.grid(row=1, column=20, padx=150)

canvas = Canvas(width=200, height=300)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 140, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=2, column=20)

#startButton
start_button = tkinter.Button(text="Start")
start_button.grid(row=5, column=10)

#resetButton
reset_button = tkinter.Button(text="Reset")
reset_button.grid(row=5, column=25)

window.mainloop()
