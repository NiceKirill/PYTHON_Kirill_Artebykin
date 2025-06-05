import sqlite3
from datetime import datetime


def create_database():
    conn = sqlite3.connect('abiturient.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Анкета (
        reg_number INTEGER PRIMARY KEY AUTOINCREMENT,
        last_name TEXT NOT NULL,
        first_name TEXT NOT NULL,
        middle_name TEXT,
        birth_date TEXT NOT NULL,
        awards TEXT CHECK(awards IN ('да', 'нет')) NOT NULL DEFAULT 'нет',
        address TEXT NOT NULL,
        specialty TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("База данных успешно создана")