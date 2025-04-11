## Средствами языка Python сформировать текстовый файл (.txt), содержащий
## последовательность из целых положительных и отрицательных чисел. Сформировать
## новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
## обработку элементов:
## Исходные данные:
## Количество элементов:
## Максимальный элемент:
## Произведение элементов меньших 0 в первой половине:

numbers = ['-98 4 77 -8 41 9 -11 -15']
f1 = open('data_1.txt', 'w')
f1.writelines(numbers)
f1.close()

f2 = open('data_2.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(numbers)
f2.close()

f1 = open('data_1.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()


f1 = open('data_1.txt')
my_max, t = 0, 1
for i in range(len(k)):
    my_max = my_max if my_max > k[i] else k[i]


for i in range(len(k) // 2):
    if k[i] < 0:
        t *= k[i]

f2 = open('data_2.txt', 'a')
f2.write('\n')
f2.write('Количество элементов: ')
f2.write(str(len(k)))
f2.write('\n')
f2.write('Максимальный элемент: ')
f2.write(str(my_max))
f2.write('\n')
f2.write('Произведение элементов меньших 0 в первой половине: ')
f2.write(str(t))

f2.close().
print('Количество элементов: ', len(k), 'Максимальный элемент: ', my_max, 'Произведение элементов меньших 0 в первой половине: ', t)