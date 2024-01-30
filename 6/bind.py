import tkinter as tk

def add_text(event):
    text = text_entry.get()
    if text != "":
        listbox.insert(tk.END, text)
        text_entry.delete(0, tk.END)

def copy_text(event):
    selected_text = listbox.get(listbox.curselection())
    text_entry.delete(0, tk.END)
    text_entry.insert(tk.END, selected_text)
window = tk.Tk()
text_entry = tk.Entry(window)
text_entry.pack()
listbox = tk.Listbox(window)
listbox.pack()
text_entry.bind('<Return>', add_text)
listbox.bind('<Double-Button-1>', copy_text)
window.mainloop()