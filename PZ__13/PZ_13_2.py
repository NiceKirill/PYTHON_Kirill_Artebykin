## В двумерном списке найти сумму отрицательных элементов в первой трети
## матрицы.

def sum_negatives_in_first_third(matrix):
    if not matrix:
        return 0

    n = len(matrix)
    first_third = n // 3
    total_sum = 0

    for i in range(first_third):
        for num in matrix[i]:
            if num < 0:
                total_sum += num

    return total_sum


# Пример
matrix = [
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9],
    [10, -11, 12],
    [-13, 14, -15],
    [16, -17, 18]
]

result = sum_negatives_in_first_third(matrix)
print(result)