import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(window, font=("Arial", 24, "bold"))

my_label.config(text="New Text")
my_label.pack()


def button_clicked():
    print("Button clicked")


button = tkinter.Button(window, text="Click Me", command=button_clicked)
button.pack()

selected_value = tkinter.IntVar()

radiobutton1 = tkinter.Radiobutton(text="option 1", variable=selected_value, value=1)
radiobutton1.pack()

radiobutton2 = tkinter.Radiobutton(text="option 2", variable=selected_value, value=2)
radiobutton2.pack()

radiobutton3 = tkinter.Radiobutton(text="option 3", variable=selected_value, value=3)
radiobutton3.pack()

radiobutton4 = tkinter.Radiobutton(text="option 4", variable=selected_value, value=4)
radiobutton4.pack()

window.mainloop()
