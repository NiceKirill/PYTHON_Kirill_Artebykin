## Составить список, в который будут включены только согласные буквы и
## привести их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль',
## 'Дели', 'Каир'].

cities = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
vowels = set('аеиоуъюяАЕИОУЪЮЯ')

result = []

for city in cities:
    consonants = [letter.upper() for letter in city if letter.upper() not in vowels]

    result.append(''.join(consonants))

print(result)