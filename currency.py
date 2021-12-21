from tkinter import *
from google_currency import convert
import json

window = Tk()
window.title("Desktop Currency Converter")
window.geometry("500x250")
window.configure(background="darkgreen")


myLabel1 = Label(window, text="Amount", bg="lightgreen", fg="black", font="calibri 12 bold")
myLabel1.pack()

input_value = Entry(window, width=30, background="white", font="calibri 12 bold")
input_value.pack()

myLabel2 = Label(window, text="From (currency): ", bg="green", fg="black", font="calibri 12 bold")
myLabel2.pack()
input_unit = Entry(window, width=30, background="white", font="calibri 12 bold")
input_unit.pack()


myLabel3 = Label(window, text="To (currency): ", bg="green", fg="black", font="calibri 12 bold")
myLabel3.pack()
output_unit = Entry(window, width=30, background="white", font="calibri 12 bold")
output_unit.pack()


def conver1():
    in1 = str(input_unit.get())
    out1 = str(output_unit.get())
    inv1 = float(input_value.get())
    y = json.loads(convert(in1, out1, inv1))
    conv_label = Label(window, text=y["amount"], bg="white", fg="black", font="none 12 bold")
    conv_label.pack()


myButton = Button(window, text="Convert", command=conver1)
myButton.pack()
window.mainloop()
