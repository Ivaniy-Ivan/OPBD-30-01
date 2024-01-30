from tkinter import *
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showerror("Ошибка", "Введите задачу!")

def delete_task():
    try:
        index = task_list.curselection()
        task_list.delete(index)
    except:
        messagebox.showerror("Ошибка", "Выберите задачу для удаления!")

def mark_task():
    try:
        index = task_list.curselection()
        task_list.itemconfig(index, fg="gray")
    except:
        messagebox.showerror("Ошибка", "Выберите задачу для отметки выполнения!")
window = Tk()
window.title("Приложение для учета задач")
task_entry = Entry(window, width=30)
task_entry.pack(pady=10)
add_button = Button(window, text="Добавить задачу", command=add_task)
add_button.pack(pady=5)
delete_button = Button(window, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)
mark_button = Button(window, text="Отметить задачу", command=mark_task)
mark_button.pack(pady=5)
task_list = Listbox(window, width=50)
task_list.pack(pady=10)
window.mainloop()