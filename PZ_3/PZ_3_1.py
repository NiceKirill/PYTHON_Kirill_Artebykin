## 1. Дано целое число A. Проверить истинность высказывания: «Число A является
## нечетным».

A = int(input('Введите число (A):'))

x = A%2

print('Число нечетно:',x==1)