import tkinter

window = tkinter.Tk()
window.minsize(width=1000, height=800)
window.title("This is a grid example")

label = tkinter.Label()
label.config(text="Example")
label.grid(column=1, row=1)

button2 = tkinter.Label()
button2.config(text="New Button")
button2.grid(column=3, row=1)

button = tkinter.Button()
button.config(text="Button")
button.grid(column=2, row=2)

textinput = tkinter.Entry()
textinput.config(width=50)
textinput.grid(column=4, row=3)

window.mainloop()
