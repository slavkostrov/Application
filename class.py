import tkinter as tk
from random import randint


root = tk.Tk()
root.geometry('500x500')
root.title('Mini-game')
root.resizable(0, 0)


def hand(event, ball):
    area.delete(ball.id_ball)

class Ball:
    global area
    id_ball, x, y, r, dx, dy = 0, 0, 0, 0, 0, 0
    def __init__(self):
        self.r = randint(25, 150)
        self.x = randint(1 + self.r, 500 - self.r)
        self.y = randint(1 + self.r, 500 - self.r)
        self.dx = 5
        self.dy = 5
        self.id_ball = 0
        area.bind('<Button-1>', lambda event, b = self: hand(event, b))
        print('Ball created')
    
    def show_on_canvas(self):
        self.id_ball = area.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = 'floral white', outline = 'blue')



def main():
    global area
    area = tk.Canvas(root, bg = 'grey')
    area.pack(expand = True, fill = tk.BOTH)
    
    a = Ball()
    a.show_on_canvas()

    root.mainloop()

main()
