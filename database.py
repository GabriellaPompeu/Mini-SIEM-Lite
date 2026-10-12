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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS file_state (
            file_path TEXT PRIMARY KEY,
            offset INT NOT NULL DEFAULT 0
        );
    """)

    connection.commit()
    connection.close()

def get_file_offset(file_path):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT offset
        FROM file_state
        WHERE file_path = ?;
    """, (file_path,))

    result = cursor.fetchone()
    connection.close()

    if result is None: return 0
    else: return result[0]

def update_file_offset(file_path, offset):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO file_state (file_path, offset)
        VALUES (?, ?)
        ON CONFLICT(file_path)
        DO UPDATE SET offset = excluded.offset;
    """, (file_path, offset))

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

def clear_logs():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM logs")

    connection.commit()
    connection.close()

