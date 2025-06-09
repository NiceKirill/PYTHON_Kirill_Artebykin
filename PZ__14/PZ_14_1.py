## Из текстового файла (writer.txt) выбрать фамилии писателей и годы жизни, а также
## произведения ими написанные. Посчитать общее количество произведений в данном
## файле.

import re


def extract_writers_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Паттерн для извлечения фамилии, инициалов, годов жизни и произведений
    pattern = re.compile(
        r'^(?P<surname>[А-Я][а-яё]+(?:-[А-Я][а-яё]+)?)\s+(?P<initials>[А-Я]\.[А-Я]\.)\((?P<years>\d{4}-\d{4})\)[^.]*\.(?P<works>.*?)(?=\n\s*[А-Я]|\Z)',
        re.MULTILINE | re.DOTALL
    )

    writers = []
    total_works = 0

    for match in pattern.finditer(content):
        surname = match.group('surname')
        initials = match.group('initials')
        years = match.group('years')
        works_text = match.group('works')

        # Извлекаем произведения
        works = []
        works_matches = re.findall(r'«([^»]+)»', works_text)
        if works_matches:
            works.extend(works_matches)

        # Проверяем на наличие "и другие" или "и многих других"
        if re.search(r'и (?:многих )?других', works_text):
            works.append("... и другие произведения")

        # Добавляем писателя в список
        writer_info = {
            'Фамилия': surname,
            'Инициалы': initials,
            'Годы жизни': years,
            'Произведения': works
        }
        writers.append(writer_info)
        total_works += len(works)

    return writers, total_works


def main():
    file_path = 'writer.txt'
    writers, total_works = extract_writers_info(file_path)

    # Вывод информации о писателях
    for i, writer in enumerate(writers, 1):
        print(f"{i}. {writer['Фамилия']} {writer['Инициалы']} ({writer['Годы жизни']})")
        if writer['Произведения']:
            print("   Произведения:")
            for work in writer['Произведения']:
                print(f"   - {work}")
        else:
            print("   Произведения: не указаны")
        print()

    # Вывод общего количества произведений
    print(f"\nОбщее количество произведений: {total_works}")


if __name__ == "__main__":
    main()