import tkinter

window = tkinter.Tk()
window.title("I'm a title")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="I'm a label!", font=("Ariel", 20))

my_label.grid(row=2, column=1)
my_label["text"] = "text 2"
my_label.config(text=0)

clicks = 0
def button_clicked():
    global clicks
    clicks += 1
    my_label.config(text=clicks)
    my_label_2.config(text=input_1.get())


button = tkinter.Button(text="I'm a button!", command=button_clicked)
button.grid(row=1, column=0)

input_1 = tkinter.Entry()
input_1.grid(row=0, column=2)
my_label_2 = tkinter.Label(text="Write something and click button!", font=("Ariel", 8))
my_label_2.grid(row=1, column=2)



window.mainloop()
