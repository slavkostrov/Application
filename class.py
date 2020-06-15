import tkinter as tk
from random import randint


root = tk.Tk()
root.geometry('500x500')
root.title('Mini-game')
root.resizable(0, 0)


def hand(event, ball):
    global count
    global t
    if count == 5:
        count = 0
        t += 1000
    if (event.x < ball.x + ball.r and event.x > ball.x - ball.r and event.y < ball.y + ball.r and event.y > ball.y - ball.r) :
        area.delete(ball.id_ball)
        count +=1

class Ball:
    global area
    id_ball, x, y, r, dx, dy = 0, 0, 0, 0, 0, 0
    def __init__(self):
        self.r = randint(25, 100)
        self.x = randint(1 + self.r, 500 - self.r)
        self.y = randint(1 + self.r, 500 - self.r)
        self.dx = 5
        self.dy = 5
        self.id_ball = 0
        area.bind('<Button-1>', lambda event, b = self: hand(event, b))
    
    def show_on_canvas(self):
        self.id_ball = area.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = 'floral white', outline = 'blue')




def tick():
    global balls
    global area
    global t
    if t > 500:
        t -= 100
    for x in balls:
        area.delete(x.id_ball)
    x = Ball()
    x.show_on_canvas()
    balls += [x]
    area.after(t, tick)


def main():
    global area
    area = tk.Canvas(root, bg = 'grey')
    area.pack(expand = True, fill = tk.BOTH)
    
    global balls
    a = Ball()
    
    global t
    t = 2000

    global count
    count = 0

    a.show_on_canvas()
    balls = [a]

    tick()

    root.mainloop()

main()
