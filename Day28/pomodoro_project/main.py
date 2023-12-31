import math
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


def count_down(count):

    count_min = math.floor(count / 60)
    count_seconds = (count % 60)
    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f"{0}{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.config(pady=50)
window.minsize(width=300, height=200)

# label
timer_label = tkinter.Label(text="Timer", font=("Arial", 32, "normal"), fg=GREEN)
timer_label.grid(row=0, column=2)

canvas = Canvas(width=200, height=300)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=2)


def start_click():
    count_down(SHORT_BREAK_MIN * 60)


# startButton
start_button = tkinter.Button(text="Start", command=start_click)
start_button.grid(row=2, column=1, padx=5)

# resetButton
reset_button = tkinter.Button(text="Reset")
reset_button.grid(row=2, column=3)

# check_mark
check_mark = tkinter.Label(text="✅")
check_mark.grid(row=3, column=2)
window.mainloop()
