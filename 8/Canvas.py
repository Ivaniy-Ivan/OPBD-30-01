
from tkinter import *

def draw_scene():
    canvas.delete('all')
    canvas.create_rectangle(50, 150, 150, 250, fill='#87CEEB', outline='')
    canvas.create_polygon(20, 150, 180, 150, 100, 100, fill='#87CEEB', outline='')
    canvas.create_oval(200, 50, 250, 100, fill='yellow', outline='')

    for i in range(0, 300, 6):
        canvas.create_arc(i, 250, i + 10, 370, start=0, extent=180, fill='green', outline='')

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()
draw_scene()
root.mainloop()