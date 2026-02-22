import sqlite3
import os

def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS parts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,           -- Наименование
                catalog_number TEXT,          -- № по каталогу
                retail_price REAL NOT NULL,   -- Розничная цена
                stock INTEGER DEFAULT 0,      -- Склад (количество)
                description TEXT,
                serial_number TEXT UNIQUE
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        # Можно добавить тестовую запись для проверки
        # conn.execute("""... INSERT ...""")
    print("✅ База данных инициализирована.")

if __name__ == "__main__":
    init_db()