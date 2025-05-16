## В двумерном списке найти сумму отрицательных элементов в первой трети
## матрицы.

import random

matrix = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]

def sum_negatives_in_first_third(matrix):
    if not matrix:
        return 0

    first_third_rows = matrix[:len(matrix) // 3]
    negatives = [num for row in first_third_rows for num in row if num < 0]
    return sum(negatives)

print("Случайная матрица:")
print(*matrix, sep='\n')

result = sum_negatives_in_first_third(matrix)
print("\nСумма отрицательных элементов в первой трети:", result)