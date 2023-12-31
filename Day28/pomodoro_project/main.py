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
reps = 0
timer_job = None  # Variable to store the current countdown job


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_job)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, timer_job

    if timer_job is not None:
        window.after_cancel(timer_job)
        timer_job = None

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        timer_label.config(text="Break", fg=GREEN)
        count_down(short_break_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Long Break", fg=PINK)
        count_down(long_break_sec)
    else:
        timer_label.config(text="Work", fg=RED)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer_job
    count_min = math.floor(count / 60)
    count_seconds = (count % 60)
    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f"{0}{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        timer_job = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✅"
        check_mark.config(text=marks)


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


# startButton
start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=1, padx=5)

# resetButton
reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=3)

# check_mark "✅"
check_mark = tkinter.Label()
check_mark.grid(row=3, column=2)
window.mainloop()
