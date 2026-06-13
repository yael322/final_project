import sqlite3

class Bot:

    @staticmethod
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

    @staticmethod
    def get_character_info(character_name):
        conn = sqlite3.connect("hsr.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM characters
            WHERE LOWER(name) = LOWER(?)
        """, (character_name,))

        result = cursor.fetchone()

        conn.close()

        if result is None:
            return "Character not found!"

        return {
            "id": result[0],
            "name": result[1],
            "rarity": result[2],
            "path": result[3],
            "element": result[4],
            "faction": result[5],
            "planet": result[6],
            "description": result[7]
        }
    
    @staticmethod
    def get_total_characters():
        conn = sqlite3.connect("hsr.db")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM characters")
        result = cursor.fetchone()[0]

        conn.close()
        return result


    @staticmethod
    def get_rarity_stats():
        conn = sqlite3.connect("hsr.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT rarity, COUNT(*)
            FROM characters
            GROUP BY rarity
        """)

        result = cursor.fetchall()

        conn.close()
        return result


    @staticmethod
    def get_element_stats():
        conn = sqlite3.connect("hsr.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT element, COUNT(*)
            FROM characters
            GROUP BY element
            ORDER BY COUNT(*) DESC
        """)

        result = cursor.fetchall()

        conn.close()
        return result
