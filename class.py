import tkinter as tk
from random import randint
from tkinter import messagebox

root = tk.Tk()
root.geometry('1000x800')
root.title('Mini-game')
root.resizable(0, 0)



def hand(event, ball):
    global count
    global t
    global score
    if count >= 10 and t < 1000:
        count = 0
        t += 1000
    if (event.x < ball.x + ball.r and event.x > ball.x - ball.r and event.y < ball.y + ball.r and event.y > ball.y - ball.r) :
        area.delete(ball.id_ball)
        balls.remove(ball)
        count +=1
        score += 1
        lbl.configure(text = str(score))

class Ball:
    global area
    id_ball, x, y, r, dx, dy = 0, 0, 0, 0, 0, 0
    def __init__(self):
        self.r = randint(25, 100)
        self.x = randint(1 + self.r, 1000 - self.r)
        self.y = randint(1 + self.r, 800 - self.r)
        self.dx = 5
        self.dy = 5
        self.id_ball = 0
        area.bind('<Button-1>', lambda event, b = self: hand(event, b))
    
    def show_on_canvas(self):
        self.id_ball = area.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = 'orchid3', outline = 'black')




def tick():
    global balls
    global area
    global t
    global score

    if score < -50:
        ans = messagebox.askyesno("You lose", "Restart?")
        if ans == False:
            exit()
        else:
            score = 0
            t = 2000
            area.delete(balls[0].id_ball)
            balls = []
    
    if score >= 100:
        ans = messagebox.askyesno("You win", "Restart?")
        if ans == False:
            exit()
        else:
            score = 0
            t = 2000
            area.delete(balls[0].id_ball)
            balls = []

    

    if t > 500:
        t -= 100
    i = 0
    for x in balls:
        area.delete(x.id_ball)
        balls.remove(x)
        i += 1
    
    if i > 0:
        score -= 10
        lbl.configure(text = str(score))
    x = Ball()
    x.show_on_canvas()
    balls += [x]
    area.after(t, tick)


def main():
    global area
    global lbl
    global score
    score = 0
    area = tk.Canvas(root, bg = 'bisque')
    area.pack(expand = True, fill = tk.BOTH)
    
    global balls
    
    global t
    t = 2000

    global count
    count = 0
    
    balls = []

    lbl = tk.Label(root, text = '0')
    lbl.place(x = 5, y = 5)

    tick()

    root.mainloop()

main()
