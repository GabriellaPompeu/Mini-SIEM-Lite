import sqlite3 as sql
from pathlib import Path
from models import LogEvent

DATABASE_PATH = Path("database") / "siem.db"

def create_connection():
    return sql.connect(DATABASE_PATH)

def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            method TEXT NOT NULL,
            endpoint TEXT NOT NULL,
            protocol TEXT NOT NULL,
            status INTEGER NOT NULL,
            size INTEGER NOT NULL
        );
    """)

    connection.commit()
    connection.close()

def insert_log(event: LogEvent):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO logs(
            ip, timestamp, method, endpoint, protocol, status, size
        ) VALUES (?, ?, ?, ?, ?, ?, ?) """,
        (event.ip, event.timestamp, event.method, event.endpoint, event.protocol, event.status, event.size))

    connection.commit()
    connection.close()
