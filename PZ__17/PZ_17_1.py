import tkinter as tk
from tkinter import ttk, messagebox


def submit_form():
    if not name_entry.get() or not email_entry.get() or not age_entry.get():
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все обязательные поля (*)")
        return

    selected_animals = []
    for animal, var in animal_vars.items():
        if var.get():
            selected_animals.append(animal)

    messagebox.showinfo("Успех", "Форма успешно отправлена!")
    print("Выбранные животные:", ", ".join(selected_animals))


root = tk.Tk()
root.title("Форма заявки на работу в зоопарке")
root.geometry("600x750")

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# Заголовок
title_label = ttk.Label(main_frame, text="Форма заявки на работу в зоопарке", font=('Arial', 14, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

note_label = ttk.Label(main_frame, text="Пожалуйста, заполните форму. Обязательные поля помечены *", font=('Arial', 10))
note_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))

contact_frame = ttk.LabelFrame(main_frame, text="Контактная информация", padding=10)
contact_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 20))

# Имя
name_label = ttk.Label(contact_frame, text="Имя *")
name_label.grid(row=0, column=0, sticky='w', padx=(0, 10))
name_entry = ttk.Entry(contact_frame, width=30)
name_entry.grid(row=0, column=1, sticky='ew')

# Телефон
phone_label = ttk.Label(contact_frame, text="Телефон")
phone_label.grid(row=1, column=0, sticky='w', padx=(0, 10), pady=(10, 0))
phone_entry = ttk.Entry(contact_frame, width=30)
phone_entry.grid(row=1, column=1, sticky='ew', pady=(10, 0))

# Email
email_label = ttk.Label(contact_frame, text="Email *")
email_label.grid(row=2, column=0, sticky='w', padx=(0, 10), pady=(10, 0))
email_entry = ttk.Entry(contact_frame, width=30)
email_entry.grid(row=2, column=1, sticky='ew', pady=(10, 0))

personal_frame = ttk.LabelFrame(main_frame, text="Персональная информация", padding=10)
personal_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 20))

# Возраст
age_label = ttk.Label(personal_frame, text="Возраст *")
age_label.grid(row=0, column=0, sticky='w', padx=(0, 10))
age_entry = ttk.Entry(personal_frame, width=30)
age_entry.grid(row=0, column=1, sticky='ew')

# Пол
gender_label = ttk.Label(personal_frame, text="Пол")
gender_label.grid(row=1, column=0, sticky='w', padx=(0, 10), pady=(10, 0))
gender_frame = ttk.Frame(personal_frame)
gender_frame.grid(row=1, column=1, sticky='w', pady=(10, 0))

gender_var = tk.StringVar()

male_radio = ttk.Radiobutton(gender_frame, text="Муж", variable=gender_var, value="Муж")
male_radio.pack(side=tk.LEFT)
female_radio = ttk.Radiobutton(gender_frame, text="Женщина", variable=gender_var, value="Женщина")
female_radio.pack(side=tk.LEFT, padx=(10, 0))

# Личные качества
qualities_label = ttk.Label(personal_frame, text="Перечислите личные качества")
qualities_label.grid(row=2, column=0, sticky='w', padx=(0, 10), pady=(10, 0))
qualities_entry = ttk.Entry(personal_frame, width=30)
qualities_entry.grid(row=2, column=1, sticky='ew', pady=(10, 0))

# Фрейм для выбора животных с рамкой
animals_frame = ttk.LabelFrame(main_frame, text="Выберите ваших любимых животных", padding=10)
animals_frame.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(0, 20))

animals = ["Зебра", "Кошак", "Анаконда", "Человек", "Слон", "Антилопа", "Голубь", "Краб"]
animal_vars = {}

animals_check_frame = ttk.Frame(animals_frame)
animals_check_frame.pack(fill='x')

for i, animal in enumerate(animals):
    animal_vars[animal] = tk.BooleanVar()
    col = i % 2
    row = i // 2

    cb = ttk.Checkbutton(animals_check_frame, text=animal, variable=animal_vars[animal])
    cb.grid(row=row, column=col, sticky='w', padx=(0, 20))

# Кнопка отправки
submit_button = ttk.Button(main_frame, text="Отправить информацию", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, pady=20)

main_frame.columnconfigure(1, weight=1)
contact_frame.columnconfigure(1, weight=1)
personal_frame.columnconfigure(1, weight=1)
animals_frame.columnconfigure(1, weight=1)

root.mainloop()