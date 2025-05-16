## В двумерном списке найти минимальный и максимальные элементы.

import random

matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

print("Случайная матрица:")
for row in matrix:
    print(row)

flattened = [num for row in matrix for num in row]  # Преобразование в одномерный список

min_val = min(flattened)
max_val = max(flattened)

print("Min элемент:", min_val)
print("Max элемент:", max_val)