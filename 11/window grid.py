import tkinter as tk


def create_shape():
    top = tk.Toplevel()
    x_label = tk.Label(top, text="X:")
    x_label.grid(row=0, column=0)
    x_entry = tk.Entry(top)
    x_entry.grid(row=0, column=1)

    y_label = tk.Label(top, text="Y:")
    y_label.grid(row=1, column=0)
    y_entry = tk.Entry(top)
    y_entry.grid(row=1, column=1)

    width_label = tk.Label(top, text="Ширина:")
    width_label.grid(row=2, column=0)
    width_entry = tk.Entry(top)
    width_entry.grid(row=2, column=1)

    height_label = tk.Label(top, text="Высота:")
    height_label.grid(row=3, column=0)
    height_entry = tk.Entry(top)
    height_entry.grid(row=3, column=1)

    shape_var = tk.StringVar()
    radiobutton1 = tk.Radiobutton(top, text="Прямоугольник", variable=shape_var, value="rectangle")
    radiobutton1.grid(row=4, column=0)
    radiobutton2 = tk.Radiobutton(top, text="Овал", variable=shape_var, value="oval")
    radiobutton2.grid(row=4, column=1)

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
    draw_button.grid(row=5, columnspan=2)


root = tk.Tk()
canvas = tk.Canvas(root, width=700, height=700)
canvas.grid(row=0, column=0, columnspan=2)

add_button = tk.Button(root, text="Добавить фигуру", command=create_shape)
add_button.grid(row=1, columnspan=2)

root.mainloop()