import tkinter as tk

def change_text_field_size(event=None):
    width = int(width_entry.get())
    height = int(height_entry.get())
    text_field.config(width=width, height=height)

def update_text_field_background(event):
    if event.type == tk.EventType.Enter:
        text_field.config(bg="white")
    elif event.type == tk.EventType.Leave:
        text_field.config(bg="lightgrey")
window = tk.Tk()
width_label = tk.Label(window, text="Ширина:")
width_label.pack()
width_entry = tk.Entry(window)
width_entry.pack()
height_label = tk.Label(window, text="Высота:")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()
text_field = tk.Text(window)
text_field.pack()
button = tk.Button(window, text="Изменить размер", command=change_text_field_size)
button.pack()
window.bind('<Return>', change_text_field_size)
text_field.bind('<FocusIn>', update_text_field_background)
text_field.bind('<FocusOut>', update_text_field_background)
window.mainloop()