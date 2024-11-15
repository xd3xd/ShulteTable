import tkinter as tk
import random

class ShulteTable:
    def __init__(self, master):
        self.master = master
        self.master.title("Таблица Шульте")

        self.size = 5
        self.numbers = list(range(1, self.size**2 + 1))
        random.shuffle(self.numbers)

        self.buttons = []
        for i in range(self.size):
            row_buttons = []
            for j in range(self.size):
                number = self.numbers[i * self.size + j]
                button = tk.Button(master, text=str(number), width=5, height=2, command=lambda num=number: self.on_click(num))
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def on_click(self, number):
        print(f"Вы нажали на число: {number}")

mainwindow = tk.Tk()
shulte_app = ShulteTable(mainwindow)
mainwindow.mainloop()