from tkinter import *
from tkinter.ttk import *

def shop():
    selectToSecond = list(lbox1.curselection())
    selectToSecond.reverse()
    for i in selectToSecond:
        lbox2.insert(END, lbox1.get(i))
    for i in selectToSecond:
        lbox1.delete(i)

def basket():
    selectToFirst = list(lbox2.curselection())
    selectToFirst.reverse()
    for i in selectToFirst:
        lbox1.insert(END, lbox2.get(i))
    for i in selectToFirst:
        lbox2.delete(i)


root = Tk()

lbox1 = Listbox(selectmode=EXTENDED)

for i in ('Ананасик','Картошка','Курица','Масло','Хлеб','Помидоры','Бананы','Яблоки'):
    lbox1.insert(END, i)

lbox1.pack(side=LEFT)

lbox2 = Listbox(selectmode=EXTENDED)
lbox2.pack(side=RIGHT)

f = Frame()
f.pack(side=LEFT, padx=10)
Button(f, text=">>>", command=shop).pack(fill=X)
Button(f, text="<<<", command=basket).pack(fill=X)

root.mainloop()