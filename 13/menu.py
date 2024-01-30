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

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=insert_text)
file_menu.add_command(label="Сохранить", command=extract_text)

context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Очистить", command=clear_text)

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

text.bind("<Button-3>", show_context_menu)

root.mainloop()