import sqlite3

def get_db():
    conn = sqlite3.connect("tickets.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            priority TEXT
        )
    """)
    return conn
