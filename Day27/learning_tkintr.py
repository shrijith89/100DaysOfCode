import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(window, font=("Arial", 24, "bold"))

my_label.config(text="New Text")
my_label.pack()
window.mainloop()
