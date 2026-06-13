import sqlite3

def create_db():
    conn = sqlite3.connect("hsr.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        rarity INTEGER,
        path TEXT,
        element TEXT,
        faction TEXT,
        planet TEXT,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()

create_db()
