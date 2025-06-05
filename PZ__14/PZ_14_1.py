## Из текстового файла (writer.txt) выбрать фамилии писателей и годы жизни, а также
## произведения ими написанные. Посчитать общее количество произведений в данном
## файле.

import re

def process_writers_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Извлечения информации о писателях
    writer_pattern = re.compile(
        r'(?P<name>[А-Я][а-я]+ [А-Я][а-я]+(?: [А-Я][а-я]+)?)\s*\((?P<years>\d{4}-\d{4})\)\s*:\s*(?P<works>.+?)(?=\n\n|\Z)',
        re.DOTALL
    )

    # Разделения произведений
    works_pattern = re.compile(r'«(.+?)»')

    writers = []
    total_works = 0

    # Поиск всех совпадений
    for match in writer_pattern.finditer(content):
        name = match.group('name')
        years = match.group('years')
        works_text = match.group('works')

        works = works_pattern.findall(works_text)
        work_count = len(works)
        total_works += work_count

        writers.append({
            'name': name,
            'years': years,
            'works': works,
            'work_count': work_count
        })

    print("Информация о писателях и их произведениях:")
    print("-" * 50)
    for writer in writers:
        print(f"Писатель: {writer['name']}")
        print(f"Годы жизни: {writer['years']}")
        print("Произведения:")
        for i, work in enumerate(writer['works'], 1):
            print(f"  {i}. {work}")
        print(f"Всего произведений: {writer['work_count']}")
        print("-" * 50)

    print(f"\nОбщее количество произведений в файле: {total_works}")

if __name__ == "__main__":
    file_path = "writer.txt"
    process_writers_file(file_path)