## Из предложенного текстового файла (text18-2.txt) вывести на экран его содержимое,
## количество знаков препинания. Сформировать новый файл, в который поместить текст в
## стихотворной форме выведя строки в обратном порядке.

# Определяем знаки препинания
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Читаем исходный файл
with open('text18-2.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    lines = file.readlines()

# Выводим содержимое файла
print("Содержимое файла:")
print(content)

# Считаем знаки препинания
punctuation_count = sum(1 for char in content if char in punctuation)
print(f"\nКоличество знаков препинания: {punctuation_count}")

# Записываем строки в обратном порядке в новый файл
with open('reversed_poem.txt', 'w', encoding='utf-8') as new_file:
    reversed_lines = reversed(content.split('\n'))
    new_file.write('\n'.join(reversed_lines))

print("\nФайл с обратным порядком строк создан: 'reversed_poem.txt'")