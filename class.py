import tkinter as tk


root = tk.Tk()
root.geometry('500x500')
root.title('Mini-game')
root.resizable(0, 0)









def main():
    area = tk.Canvas(root, bg = 'yellow')
    area.pack(expand = True, fill = tk.BOTH)
    root.mainloop()

main()
