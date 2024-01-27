from tkinter import *

window = Tk()
window.title("Miles to Km converter")

window.minsize(width=500, height=300)
window.config(pady=30)
window.config(padx=30)


def button_clicked():
    number = entry.get()
    new_number = int(number)*1.609
    label_2.config(text=new_number)


my_label = Label(text="is equal to", font=("Arial", 12,))
my_label.grid(column=0, row=1)

label_2 = Label(text="0", font=("Arial", 12))
label_2.grid(column=1, row=1)

label_3 = Label(text="miles", font=("Arial", 12))
label_3.grid(column=3, row=0)

label_4 = Label(text="km", font=("Arial", 12))
label_4.grid(column=3, row=1)

entry = Entry(width=30)
entry.get()
entry.grid(column=1, row=0)
window.bind('<Return>', lambda event=None: button_clicked())

button = Button(text="calculate", command=button_clicked)
button.grid(column=1, row=2)






window.mainloop()