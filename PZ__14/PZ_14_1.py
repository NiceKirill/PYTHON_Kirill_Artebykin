## Из текстового файла (writer.txt) выбрать фамилии писателей и годы жизни, а также
## произведения ими написанные. Посчитать общее количество произведений в данном
## файле.

import re

total_works = 0
writers_info = []

with open('writer.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # Регулярное выражение для извлечения данных
        match = re.match(r"(.+?) \((\d{4}-\d{4})\): (.+)", line.strip())
        if match:
            name = match.group(1)
            years = match.group(2)
            works = [work.strip() for work in match.group(3).split(',')]

            writers_info.append({
                'name': name,
                'years': years,
                'works': works
            })

            total_works += len(works)

for writer in writers_info:
    print(f"{writer['name']} ({writer['years']}): {', '.join(writer['works'])}")

print(f"\nОбщее количество произведений: {total_works}")