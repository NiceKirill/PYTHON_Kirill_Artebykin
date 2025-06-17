## Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
## информацию из строки в словарь, найти среднее арифметическое оценок,
## результаты вывести на экран.

import tkinter as tk
from tkinter import ttk

def process_data():
    input_str = input_entry.get()
    parts = input_str.split()

    if len(parts) < 4:
        result_label.config(text="Ошибка: недостаточно данных в строке")
        return

    try:
        data = {
            "Фамилия": parts[0],
            "Имя": parts[1],
            "Группа": parts[2],
            "Оценки": list(map(int, parts[3:]))
        }

        avg = sum(data["Оценки"]) / len(data["Оценки"])

        result_text = f"Данные:\n{data}\n\nСредний балл: {avg:.2f}"
        result_label.config(text=result_text)

    except ValueError:
        result_label.config(text="Ошибка: некорректные данные в строке")


root = tk.Tk()
root.title("Обработка данных студента")
root.geometry("500x400")

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Заголовок
title_label = ttk.Label(main_frame, text="Обработка данных студента", font=('Arial', 14, 'bold'))
title_label.grid(row=0, column=0, pady=(0, 20))

# Ввод данных
input_label = ttk.Label(main_frame, text="Введите строку данных:")
input_label.grid(row=1, column=0, sticky='w')

input_entry = ttk.Entry(main_frame, width=50)
input_entry.grid(row=2, column=0, sticky='ew', pady=(0, 20))
input_entry.insert(0, "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4")

# Кнопка обработки
process_button = ttk.Button(main_frame, text="Обработать", command=process_data)
process_button.grid(row=3, column=0, pady=(0, 20))

# Результат
result_label = ttk.Label(main_frame, text="", wraplength=400, justify='left')
result_label.grid(row=4, column=0, sticky='w')

main_frame.columnconfigure(0, weight=1)

root.mainloop()