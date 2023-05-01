import sqlite3

from moneyminds.model import Carteira


conn = sqlite3.connect('moneyminds.db')
cursor = conn.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS carteira (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            valor REAL NOT NULL,
            categoria TEXT NOT NULL,
            data TEXT NOT NULL,
            descricao TEXT NOT NULL
        );
    """)






