##Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
##деления определить, имеются ли в записи числа N нечетные цифры. Если имеются,
##то вывести TRUE, если нет — вывести FALSE.

def has_odd_digit(N):
    # Цикл, который выполняется, пока N больше 0
    while N > 0:
        # Извлечение последней цифры числа N с помощью операции остатка от деления
        last_digit = N % 10

        # Проверка, является ли последняя цифра нечетной
        if last_digit % 2 != 0:
            # Если найдена нечетная цифра, возвращаем 'TRUE'
            return 'TRUE'

        # Убираем последнюю цифру из N, используя целочисленное деление
        N //= 10

    # Если все цифры были четными, возвращаем 'FALSE'
    return 'FALSE'

try:
   # Чтение целого числа N из ввода
   N = int(input("Введите целое число N (>0): "))

   # Проверка, что N положительное
   if N <= 0:
       raise ValueError("Число должно быть больше 0.")

   # Вывод результата проверки на наличие нечетных цифр
   print(has_odd_digit(N))

except ValueError as e:
     # Обработка ошибки, если ввод некорректен
     print('Ошибка:', e)