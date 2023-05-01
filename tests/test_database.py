import sqlite3
from moneyminds.model import Carteira

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

def setup_function():
    create_table()

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

def test_create_table():
    # Verifica se a tabela foi criada corretamente
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='carteira';")
    assert cursor.fetchone()[0] == 'carteira'
