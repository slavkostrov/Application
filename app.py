import tkinter as tk
from tkinter import messagebox

def hand1(event):
    label_1.config(text = "LOOOOL")

def hand2(event):
    label_1.config(text = "Hello world")

def hand3(event):
    label_1.config(fg = 'Blue', bg = 'Yellow')

def hand4(event):
    if inp_1.index('end') != 0 and inp_2.index('end') != 0:
        first, second = int(inp_1.get()), int(inp_2.get())
        inp_1.delete(0, 'end')
        inp_2.delete(0, 'end')
        inp_1.insert(0, '0')
        inp_2.insert(0, '0')
        messagebox.showinfo("Result", str(first + second))
    else:
        messagebox.showinfo("Error", 'Entry values') 


root = tk.Tk()
root.title("First program on Python")
root.geometry('500x500')
root.resizable(0, 0)


inp_1 = tk.Entry(root, width = 20)
inp_1.insert(1, '0')
inp_1.place(x = 200, y = 200, width = 50 , height = 25)
inp_2 = tk.Entry(root, width = 20, text = '0')
inp_2.insert(1, '0')
inp_2.place(x = 250, y = 200, width = 50, height = 25)


label_1 = tk.Label(root, text = "Hello, world!", font = "Times 20")
label_1.grid(column = 0, row = 0)

button_1 = tk.Button(root, text = "Run", bg = 'gray')

button_1.place(x = 150 , y = 400, width = 200, height = 50)
button_1.bind('<Enter>', hand1)
button_1.bind('<Leave>', hand2)
button_1.bind('<Button-1>', hand4)

root.mainloop()
