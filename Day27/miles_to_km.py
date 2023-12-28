import tkinter

window = tkinter.Tk()
window.minsize(width=400, height=100)
window.title("Mile to KM Converter")

textarea = tkinter.Entry()
textarea.config(width=30)
textarea.grid(row=0, column=3, pady=20, padx=50)

km_label = tkinter.Label(text="0"+" "+"Kms")
km_label.grid(row=3, column=3)


def calculate_km():
    value = int(textarea.get())*1.60934
    km_label.config(text=f"{value} Kms")
    km_label.grid(row=3, column=3)


miles_label = tkinter.Label()
miles_label.config(text="Miles")
miles_label.grid(row=0, column=7)


label = tkinter.Label()
label.config(text="is equal to")
label.grid(row=3, column=1)


button = tkinter.Button(text="Click Me", command=calculate_km)
button.config(text="Calculate")
button.grid(row=4, column=3)

window.mainloop()
