import tkinter as tk

def create_shape():
    top = tk.Toplevel()

    x_label = tk.Label(top, text="X:")
    x_label.pack()

    x_entry = tk.Entry(top)
    x_entry.pack()

    y_label = tk.Label(top, text="Y:")
    y_label.pack()

    y_entry = tk.Entry(top)
    y_entry.pack()

    width_label = tk.Label(top, text="Ширина:")
    width_label.pack()

    width_entry = tk.Entry(top)
    width_entry.pack()

    height_label = tk.Label(top, text="Высота:")
    height_label.pack()

    height_entry = tk.Entry(top)
    height_entry.pack()

    shape_var = tk.StringVar()
    radiobutton1 = tk.Radiobutton(top, text="Прямоугольник", variable=shape_var, value="rectangle")
    radiobutton1.pack()

    radiobutton2 = tk.Radiobutton(top, text="Овал", variable=shape_var, value="oval")
    radiobutton2.pack()

    def draw_shape():
        x = int(x_entry.get())
        y = int(y_entry.get())
        width = int(width_entry.get())
        height = int(height_entry.get())
        shape_type = shape_var.get()

        if shape_type == "rectangle":
            canvas.create_rectangle(x, y, x + width, y + height)
        elif shape_type == "oval":
            canvas.create_oval(x, y, x + width, y + height)

        top.destroy()

    draw_button = tk.Button(top, text="Нарисовать", command=draw_shape)
    draw_button.pack()

root = tk.Tk()

canvas = tk.Canvas(root, width=700, height=700)
canvas.pack()

add_button = tk.Button(root, text="Добавить фигуру", command=create_shape)
add_button.pack()

root.mainloop()
