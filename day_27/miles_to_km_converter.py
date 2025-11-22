import tkinter

window = tkinter.Tk()
window.title("miles to km converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=30)

miles_label = tkinter.Label(text="miles", font=("Ariel", 10))
miles_label.grid(row=0, column=2)
km_label = tkinter.Label(text="km", font=("Ariel", 10))
km_label.grid(row=1, column=2)
is_equal_label = tkinter.Label(text="is equal to", font=("Ariel", 10))
is_equal_label.grid(row=1, column=0)
result_label = tkinter.Label(text=0, font=("Ariel", 10))
result_label.grid(row=1, column=1)


def button_clicked():
    miles = float(input_miles.get())
    km = miles*1.609
    result_label.config(text=km)


button = tkinter.Button(text="convert", command=button_clicked)
button.grid(row=2, column=1)

input_miles = tkinter.Entry()
input_miles.insert(index=0, string="0")
input_miles.grid(row=0, column=1)



window.mainloop()
