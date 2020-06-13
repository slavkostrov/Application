import tkinter as tk
from random import randint


root = tk.Tk()
root.geometry('500x500')
root.title('Mini-game')
root.resizable(0, 0)


class Ball:
    global area
    x, y, r, dx, dy = 0, 0, 0, 0, 0
    def __init__(self):
        self.r = randint(25, 150)
        self.x = randint(1 + self.r, 500 - self.r)
        self.y = randint(1 + self.r, 500 - self.r)
        self.dx = 5
        self.dy = 5
        print('Ball created')
    
    def show_on_canvas(self):
        area.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = 'floral white', outline = 'blue')



def main():
    global area
    area = tk.Canvas(root, bg = 'grey')
    area.pack(expand = True, fill = tk.BOTH)
    
    Ball().show_on_canvas()

    root.mainloop()

main()
