## Приложение АБИТУРИЕНТ для автоматизации работы приемной комиссии,
## которая обеспечивает обработку анкетных данных абитуриентов. Таблица Анкета
## содержит следующие данные об абитуриентах: Регистрационный номер, Фамилия, Имя,
## Отчество, Дата Рождения, Награды (наличие кр. Диплома или медали (да/нет)), Адрес,
## выбранная Специальность.

import sqlite3
from datetime import datetime

class AbiturientApp:
    def __init__(self):
        self.conn = sqlite3.connect('abiturient.db')
        self.cursor = self.conn.cursor()

    def add_abiturient(self):
        print("\nДобавление нового абитуриента")
        last_name = input("Фамилия: ")
        first_name = input("Имя: ")
        middle_name = input("Отчество (если нет - оставьте пустым): ")

        while True:
            birth_date = input("Дата рождения (ДД.ММ.ГГГГ): ")
            try:
                datetime.strptime(birth_date, '%d.%m.%Y')
                break
            except ValueError:
                print("Неверный формат даты. Попробуйте снова.")

        awards = input("Наличие наград (кр. диплома или медали) (да/нет): ").lower()
        while awards not in ['да', 'нет']:
            print("Пожалуйста, введите 'да' или 'нет'")
            awards = input("Наличие наград (кр. диплома или медали) (да/нет): ").lower()

        address = input("Адрес: ")
        specialty = input("Выбранная специальность: ")

        self.cursor.execute('''
        INSERT INTO Анкета (last_name, first_name, middle_name, birth_date, awards, address, specialty)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (last_name, first_name, middle_name, birth_date, awards, address, specialty))

        self.conn.commit()
        print("Абитуриент успешно добавлен!")

    def view_abiturients(self):
        print("\nСписок абитуриентов:")
        self.cursor.execute('SELECT * FROM Анкета')
        abiturients = self.cursor.fetchall()

        if not abiturients:
            print("Нет данных об абитуриентах")
            return

        for abiturient in abiturients:
            print(f"""
Регистрационный номер: {abiturient[0]}
ФИО: {abiturient[1]} {abiturient[2]} {abiturient[3] or ''}
Дата рождения: {abiturient[4]}
Награды: {abiturient[5]}
Адрес: {abiturient[6]}
Специальность: {abiturient[7]}
            """)

    def search_abiturient(self):
        print("\nПоиск абитуриента")
        search_term = input("Введите фамилию, имя или регистрационный номер: ")

        try:
            reg_number = int(search_term)
            self.cursor.execute('SELECT * FROM Анкета WHERE reg_number = ?', (reg_number,))
        except ValueError:
            self.cursor.execute('''
            SELECT * FROM Анкета 
            WHERE last_name LIKE ? OR first_name LIKE ?
            ''', (f'%{search_term}%', f'%{search_term}%'))

        results = self.cursor.fetchall()

        if not results:
            print("Абитуриенты не найдены")
            return

        for abiturient in results:
            print(f"""
Регистрационный номер: {abiturient[0]}
ФИО: {abiturient[1]} {abiturient[2]} {abiturient[3] or ''}
Дата рождения: {abiturient[4]}
Награды: {abiturient[5]}
Адрес: {abiturient[6]}
Специальность: {abiturient[7]}
            """)

    def delete_abiturient(self):
        self.view_abiturients()
        reg_number = input("\nВведите регистрационный номер абитуриента для удаления: ")

        try:
            reg_number = int(reg_number)
        except ValueError:
            print("Неверный формат регистрационного номера")
            return

        self.cursor.execute('DELETE FROM Анкета WHERE reg_number = ?', (reg_number,))
        self.conn.commit()

        if self.cursor.rowcount > 0:
            print("Абитуриент успешно удален")
        else:
            print("Абитуриент с таким номером не найден")

    def generate_report(self):
        print("\nГенерация отчетов")
        print("1. Список всех абитуриентов")
        print("2. Список абитуриентов с наградами")
        print("3. Список абитуриентов по специальности")

        choice = input("Выберите тип отчета (1-3): ")

        if choice == '1':
            self.view_abiturients()
        elif choice == '2':
            self.cursor.execute('SELECT * FROM Анкета WHERE awards = "да"')
            abiturients = self.cursor.fetchall()

            if not abiturients:
                print("Нет абитуриентов с наградами")
                return

            print("\nАбитуриенты с наградами:")
            for abiturient in abiturients:
                print(f"{abiturient[1]} {abiturient[2]} - {abiturient[7]}")
        elif choice == '3':
            specialty = input("Введите специальность для фильтра: ")
            self.cursor.execute('SELECT * FROM Анкета WHERE specialty LIKE ?', (f'%{specialty}%',))
            abiturients = self.cursor.fetchall()

            if not abiturients:
                print(f"Нет абитуриентов по специальности '{specialty}'")
                return

            print(f"\nАбитуриенты по специальности '{specialty}':")
            for abiturient in abiturients:
                print(f"{abiturient[1]} {abiturient[2]} - {abiturient[7]}")
        else:
            print("Неверный выбор")

    def run(self):
        while True:
            print("\nПриложение 'АБИТУРИЕНТ'")
            print("1. Добавить абитуриента")
            print("2. Просмотреть всех абитуриентов")
            print("3. Поиск абитуриента")
            print("4. Удалить абитуриента")
            print("5. Сформировать отчет")
            print("6. Выход")

            choice = input("Выберите действие (1-6): ")

            if choice == '1':
                self.add_abiturient()
            elif choice == '2':
                self.view_abiturients()
            elif choice == '3':
                self.search_abiturient()
            elif choice == '4':
                self.delete_abiturient()
            elif choice == '5':
                self.generate_report()
            elif choice == '6':
                print("Выход из программы")
                self.conn.close()
                break
            else:
                print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    app = AbiturientApp()
    app.run()