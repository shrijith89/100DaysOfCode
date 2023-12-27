import tkinter

window = tkinter.Tk()
window.minsize(width=500, height=300)
window.title("Learning Inputs")

label = tkinter.Label(text="Text to be changed")
label.pack()


def button_action():
    label.config(text=example.get())
    label.pack()


button = tkinter.Button(text="Click Me", command=button_action)
button.pack()


example = tkinter.Entry()
example.pack()


window.mainloop()
