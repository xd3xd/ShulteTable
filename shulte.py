import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import time

def val(n):
    while True:
        try:
            n = int(input(n))
            if int(n) > 0:
                return n
            else:
                n = input("Введите натуральное число: ")
        except:
            n = input("Вы ввели не число. Введите снова: ")

def get_table_size():
    while True:
        size_width_input = simpledialog.askstring("Размер таблицы Шульте", "Введите размер таблицы по ширине:")
        size_lenght_input = simpledialog.askstring("Размер таблицы Шульте", "Введите размер таблицы по высоте:")

        if (size_width_input is None) or (size_lenght_input is None):
            return None

        if size_width_input.isdigit() and (size_lenght_input.isdigit()):
            size_width_input = int(size_width_input)
            size_lenght_input = int(size_lenght_input)
            if (size_width_input > 0) and (size_lenght_input > 0):
                return size_width_input, size_lenght_input
            else:
                messagebox.showerror("Ошибка", "Размер таблицы должен быть положительным числом.")
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число.")
        
        return [size_width_input, size_lenght_input]

class ShulteTable:
    def __init__(self, master):
        self.master = master
        self.master.title("Таблица Шульте")

        self.rows = n
        self.columns = m
        self.numbers = list(range(1, n * m + 1))
        random.shuffle(self.numbers)

        self.start_time = None
        self.current_number = 1
        self.last_number = self.rows * self.columns

        self.labels = {}
        k = 0

        for i in range(self.rows):
            for j in range(self.columns):
                number = self.numbers[k]
                label = tk.Label(master, text=str(number), width=5, height=2, borderwidth=2, relief='groove')
                label.grid(row=i, column=j, padx=5, pady=5)
                label.bind("<Button-1>", lambda event, num=number: self.on_click(num))
                self.labels[number] = label
                k += 1

    def on_click(self, number):
        if number == 1 and self.start_time is None:
            self.start_time = time.time()
            print("Вы начали! Время запущено.")
        
        if number == self.last_number and self.current_number == self.last_number:
            if self.start_time is not None:
                elapsed_time = time.time() - self.start_time
                print(f"Вы закончили! Время: {elapsed_time:.2f} секунд.")
        elif number == self.current_number:
            self.current_number += 1
            label = self.labels[number]
            label.config(fg = 'white')
            label.unbind("<Button-1>")
        else:
            print(f"Ошибка! Вы должны нажать {self.current_number}.")

table_size = get_table_size()
if table_size is not None:
    n = table_size[0]
    m = table_size[1]

mainwindow = tk.Tk()
shulte_app = ShulteTable(mainwindow)
mainwindow.mainloop()