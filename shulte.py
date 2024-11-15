import tkinter as tk
from tkinter import messagebox
import random
import time

class ShulteTable:
    def __init__(self, master):
        self.master = master
        self.master.title("Таблица Шульте")

        self.size = 5
        self.numbers = list(range(1, self.size**2 + 1))
        random.shuffle(self.numbers)

        self.start_time = None
        self.last_number = self.size**2
        self.current_number = 1

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
        if number == 1 and self.start_time is None:
            self.start_time = time.time()
            print("Вы начали! Время запущено.")

        if number == self.last_number:
            if self.start_time is not None:
                elapsed_time = time.time() - self.start_time
                print(f"Вы закончили! Время: {elapsed_time:.2f} секунд.")
        elif number == self.current_number:
            self.current_number += 1

mainwindow = tk.Tk()
shulte_app = ShulteTable(mainwindow)
mainwindow.mainloop()