from tkinter import *
root = Tk()
root.title('Проект')

def red():
    e.delete(0, END)
    e.insert(0, '#ff0000')
    label1.config(text="красный")

def orange():
    e.delete(0, END)
    e.insert(0, '#ff7d00')
    label1.config(text='оранжевый')

def yellow():
    e.delete(0, END)
    e.insert(0, '#ffff00')
    label1.config(text='желтый')

def green():
    e.delete(0, END)
    e.insert(0, '#00ff00')
    label1.config(text='зеленый')

def blue():
    e.delete(0, END)
    e.insert(0, '#007dff')
    label1.config(text='голубой')

def darkblue():
    e.delete(0, END)
    e.insert(0, '#0000ff')
    label1.config(text='синий')

def purple():
    e.delete(0, END)
    e.insert(0, '#7d00ff')
    label1.config(text='фиолетовый')
e = Entry(width=35,bd=5, justify=CENTER)

label1 = Label(text="Вывод",width=30, bd=5)
red1 = Button(fg="white",bg="#ff0000", width=1,bd=10)
orange1 = Button( fg="white",bg="#ff7d00", width=1,bd=10)
yellow1 = Button(fg="white", bg="#ffff00", width=1,bd=10)
green1 = Button(fg="white",bg="#00ff00", width=1,bd=10)
blue1 = Button(fg="white",bg="#007dff", width=1,bd=10)
darkblue1 = Button(fg="white",bg="#0000ff", width=1,bd=10)
purple1 = Button(fg="white",bg="#7d00ff", width=1,bd=10)

red1.config(command=red)
yellow1.config(command=yellow)
orange1.config(command=orange)
green1.config(command=green)
blue1.config(command=blue)
darkblue1.config(command=darkblue)
purple1.config(command=purple)

label1.pack()
e.pack()
red1.pack(side='left',  expand=True)
yellow1.pack(side='left',  expand=True)
orange1.pack(side='left',  expand=True)
green1.pack(side='left',  expand=True)
blue1.pack(side='left',  expand=True)
darkblue1.pack(side='left',  expand=True)
purple1.pack(side='left',  expand=True)
root.mainloop()
