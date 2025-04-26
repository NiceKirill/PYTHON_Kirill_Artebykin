## В двумерном списке найти минимальный и максимальные элементы.

matrix = [
    [3, 5, 1],
    [9, 2, 8],
    [4, 6, 7]
]

flattened = [num for row in matrix for num in row]  # Преобразование в одномерный список

min_val = min(flattened)
max_val = max(flattened)

print("Min элемент:", min_val)
print("Max элемент:", max_val)