## Составить функцию, которая напечатает сорок любых символов.

import random

def print_random_chars():

    # Создаем строку с 40 случайными символами
    chars = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(40))

    # Исключение: искусственно вызываем ошибку
    if len(chars) != 40:
        raise ValueError("Неправильная длина строки")

    # Печатаем строку
    print(chars)

# Вызов функции
print_random_chars()

