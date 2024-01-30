import tkinter as tk

class AnimationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Animation")

        # Создаем холст для рисования
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        # Создаем круг, который будет анимироваться
        self.circle = self.canvas.create_oval(180, 180, 220, 220, fill="red")

        # Переменная для хранения состояния анимации
        self.animating = False

        # Создаем кнопки управления
        self.start_button = tk.Button(root, text="Start", command=self.start_animation)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_animation)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Создаем ползунок для управления скоростью анимации
        self.speed_scale = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, label="Animation Speed")
        self.speed_scale.set(5)  # Устанавливаем начальную скорость
        self.speed_scale.pack(side=tk.LEFT, padx=5)

    def start_animation(self):
        self.animating = True
        self.animate()

    def stop_animation(self):
        self.animating = False

    def animate(self):
        if self.animating:
            # Получаем текущую скорость анимации из ползунка
            speed = self.speed_scale.get()
            # Перемещаем круг
            self.canvas.move(self.circle, speed, speed)
            # Получаем координаты круга
            x1, y1, x2, y2 = self.canvas.coords(self.circle)
            # Проверяем, достиг ли круг края холста
            if x2 > self.canvas.winfo_width() or y2 > self.canvas.winfo_height():
                # Если достиг, меняем направление движения
                self.canvas.move(self.circle, -2 * speed, -2 * speed)
            # Запускаем следующий кадр анимации
            self.root.after(100 // speed, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimationApp(root)
    root.mainloop()