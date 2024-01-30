from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def insert_text():
    try:
        file_name = fd.askopenfilename()
        if file_name:
            f = open(file_name)
            s = f.read()
            text.insert(1.0, s)
            f.close()
        else:
            mb.showinfo("Ошибка", "Файл не загружен")
    except FileNotFoundError:
        mb.showinfo("Ошибка", "Файл не найден")


def extract_text():
    try:
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        if file_name:
            f = open(file_name, 'w')
            s = text.get(1.0, END)
            f.write(s)
            f.close()
        else:
            mb.showinfo("Ошибка", "Файл не сохранен")
    except FileExistsError:
        mb.showinfo("Ошибка", "Файл уже существует")


def clear_text():
    if mb.askyesno("Подтверждение", "Вы уверены, что хотите очистить текст?"):
        text.delete(1.0, END)


root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extract_text)
b2.grid(row=1, column=1, sticky=W)
b3 = Button(text="Очистить", command=clear_text)
b3.grid(row=2, columnspan=2)

root.mainloop()