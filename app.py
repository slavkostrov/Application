from tkinter import *

def hand1(event):
    label_1.config(text = "LOOOOL")

def hand2(event):
    label_1.config(text = "Hello world")

def hand3(event):
    label_1.config(fg = 'Blue', bg = 'Yellow')

root = Tk()
root.title("First program on Python")
root.geometry('500x500')
root.resizable(0, 0)

label_1 = Label(root, text = "Hello, world!", font = "Times 20")
label_1.grid(column = 0, row = 0)

button_1 = Button(root, text = "Run", bg = 'gray')

button_1.place(x = 150 , y = 400, width = 200, height = 50)
button_1.bind('<Enter>', hand1)
button_1.bind('<Leave>', hand2)
button_1.bind('<Button-1>', hand3)

root.mainloop()
