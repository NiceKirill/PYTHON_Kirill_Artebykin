## Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
## Добавьте методы для вычисления среднего балла и определения, является ли студент
## отличником.

class Student:
    def __init__(self, first_name, last_name, grades=None):

        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):

        if 1 <= grade <= 5:
            self.grades.append(grade)
        else:
            print("Оценка должна быть в диапазоне от 1 до 5")

    def get_average_grade(self):

        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def is_excellent_student(self, threshold=4.5):
        return self.get_average_grade() >= threshold

    def __str__(self):
        return f"Студент: {self.first_name} {self.last_name}, Средний балл: {self.get_average_grade():.2f}"


# Пример использования класса
if __name__ == "__main__":
    student1 = Student("Иван", "Иванов", [5, 4, 5, 5, 4])

    student1.add_grade(5)

    print(student1)

    if student1.is_excellent_student():
        print("Этот студент - отличник!")
    else:
        print("Этот студент не отличник.")

    student2 = Student("Петр", "Петров")
    student2.add_grade(3)
    student2.add_grade(4)
    student2.add_grade(3)

    print(f"\n{student2}")
    print("Отличник?", "Да" if student2.is_excellent_student() else "Нет")