import tkinter

window = tkinter.Tk()
window.minsize(width=500, height=300)
window.title("Learning Inputs")

label = tkinter.Label(text="Enter Something")
label.pack()

example = tkinter.Entry()
example.pack()
window.mainloop()
