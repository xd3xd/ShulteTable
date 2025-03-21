import tkinter as tk
import random
import time
import sys




def get_two_variables():
    def submit():
        while True:
            var1 = entry_var1.get()
            var2 = entry_var2.get()

            if (var1.strip("-").isdigit()) and (var2.strip("-").isdigit()):
                var1 = int(var1)
                var2 = int(var2)

                if (var1 > 0) and (var2 > 0):
                    root.quit()
                    button_submit.destroy()
                    return var1, var2
                else:
                    label_error1.pack(pady = 5)
                    label_error1["text"] = "Введите положительные значения"
                    root.update()
                    pass
            else:
                label_error1.pack(pady = 5)
                label_error1["text"] = "Введите числовые значения"
                root.update()
                pass

    root = tk.Tk()
    root.title("Введите размеры таблицы")
    root.resizable(False,False)
    root.geometry("200x225+100+100")

    label_var1 = tk.Label(root, text="Ширина таблицы:")
    label_var1.pack(pady=5)
    entry_var1 = tk.Entry(root)
    entry_var1.pack(pady=5)

    label_var2 = tk.Label(root, text="Высота таблицы:")
    label_var2.pack(pady=5)
    entry_var2 = tk.Entry(root)
    entry_var2.pack(pady=5)

    button_submit = tk.Button(root, text="Подтвердить", command=submit)
    button_submit.pack(pady=20)

    label_error1 = tk.Label(root, text="")

    root.mainloop()

    return int(entry_var1.get()), int(entry_var2.get())

def info():
    global k, timer_running, start_game, end_game, main, curr_num

    def start_game():
        global start_time, timer_running
        start_time = time.time()
        timer_running = True
        update_timer()
    
    def end_game():
        global timer_running
        timer_running = False
        elapsed_time = time.time() - start_time
        timer_label.config(text = f"Вы закончили! Время: {elapsed_time:.2f} секунд")
        error_label.config(text = f"")

    def update_timer():
        if timer_running:
            elapsed_time = time.time() - start_time
            timer_label.config(text=f"Время: {elapsed_time:.2f} секунд")
            error_label.config(text=f"Следующее число: {curr_num}")
            info_root.after(100, update_timer)

    def exit():
        sys.exit()

    info_root = tk.Tk()
    info_root.title("Информация")
    info_root.resizable(False, False)
    info_root.geometry("310x150+800+100")

    timer_label = tk.Label(info_root, text="Время: 0.00 секунд", font=("Times New Roman", 14, "bold"))
    timer_label.pack(pady = 10)

    error_label = tk.Label(info_root, text=f"Следующее число: {curr_num}")
    error_label.pack(pady = 10)
    
    button_exit = tk.Button(info_root, text="Выйти", command=exit)
    button_exit.pack(pady = 5)

class ShulteTable:
    def __init__(self, master):
        self.master = master
        self.master.title("Таблица Шульте")
        self.master.resizable(False,False)
        self.master.geometry("+400+100")
    
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
        global start_game, end_game, curr_num

        if number == 1 and self.start_time is None:
            start_game()
        
        if number == self.last_number and self.current_number == self.last_number:
            label = self.labels[number]
            label.config(fg = 'white')
            label.unbind("<Button-1>")
            end_game()

        elif number == self.current_number:
            self.current_number += 1
            curr_num = self.current_number
            label = self.labels[number]
            label.config(fg = 'white')
            label.unbind("<Button-1>")


start_time = 0
timer_running = False
curr_num = 1

n, m = get_two_variables()
mainwindow = tk.Tk()
shulte_app = ShulteTable(mainwindow)
info_w = info()
mainwindow.mainloop()
