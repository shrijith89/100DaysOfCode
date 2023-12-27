import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(window, font=("Arial", 24, "bold"))


def button_clicked():
    my_label.config(text="Button Clicked")
    my_label.pack()


button = tkinter.Button(window, text="Click Me", command=button_clicked)
button.pack()

window.mainloop()