import sqlite3 as sql
from database import create_table
from models import LogEvent

def main():
    create_table()
    print("Banco de dados criado")

if __name__ == "__main__":
    main()