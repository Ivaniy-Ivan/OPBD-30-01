from tkinter import *
from tkinter import filedialog
root = Tk()
root.title('Редактор')
def open():
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as f:
                text.delete('1.0', END)
                text.insert(END, f.read ())
def save():
        file_path = entry.get()
        if file_path:
            with open(file_path, 'w') as f:
                f.write(text.get('1.0', END))
                text.delete('1.0', END)
                entry.delete(0, END)
entry_frame = Frame(root)
entry_frame.pack(fill=X)
Label(entry_frame, text='Имя файла').pack(side=LEFT)
entry = Entry(entry_frame)
entry.pack(side=LEFT, fill=X, expand=True)
text = Text(root)
text.pack(fill=BOTH, expand=True)
button_frame = Frame(root)
button_frame.pack(fill=X)
Button(button_frame, text='Открыть', command=open, bd=5).pack(side=LEFT)
Button(button_frame, text='Сохранить', command=save, bd=5).pack(side=LEFT)
root.mainloop()