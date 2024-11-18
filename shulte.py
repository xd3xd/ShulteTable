import tkinter as tk
from tkinter import messagebox
import random
import time

def val(n):
    while True:
        try:
            n = int(n)
            if int(n)>=1:
                return int(n)
            else:
                n = input("Введите натуральное число: ")
        except:
            n = input("Вы ввели не число. Введите снова: ")

class ShulteTable:
    def __init__(self, master):
        self.master = master
        self.master.title("Таблица Шульте")

        self.rows = n
        self.columns = m
        self.numbers = list(range(1, n*m + 1))
        random.shuffle(self.numbers)

        self.start_time = None
        self.last_number = int(self.rows) * int(self.columns)
        self.current_number = 1

        self.buttons = []
        k = 0
        for i in range(int(self.rows)):
            row_buttons = []
            for j in range(int(self.columns)):
                number = self.numbers[k]
                button = tk.Button(master, text=str(number), width=5, height=2, command=lambda num=number: self.on_click(num))
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
                k+=1
        self.buttons.append(row_buttons)

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
        else:
            print(f"Ошибка! Вы должны нажать {self.current_number}.")

n = input("Введите размер поля по ширине: ")
n = val(n)
m = input("Введите размер поля по высоте: ")
m = val(m)

mainwindow = tk.Tk()
shulte_app = ShulteTable(mainwindow)
mainwindow.mainloop()