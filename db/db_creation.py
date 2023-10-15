import sqlite3

from settings import CONTRACT_STATUSES


def create_contract_table() -> None:
    with sqlite3.connect("database.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS contract ("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "contract_number TEXT NOT NULL,"
                       "status TEXT NOT NULL,"
                       "contact_client TEXT NOT NULL,"
                       "sign_date TEXT NOT NULL,"
                       "expire_date TEXT NOT NULL,"
                       "FOREIGN KEY (status) REFERENCES contract_status(status),"
                       "FOREIGN KEY (contact_client) REFERENCES client(client_name))")


def create_contract_status_table() -> None:
    with sqlite3.connect("database.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS contract_status ("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "status TEXT UNIQUE NOT NULL)")


def create_client_table() -> None:
    with sqlite3.connect("database.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS client ("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "client_name TEXT UNIQUE NOT NULL)")


def insert_statuses(statuses: list[str]) -> None:
    with sqlite3.connect("database.sqlite3") as connection:
        cursor = connection.cursor()
        for status in statuses:
            cursor.execute(f'INSERT OR IGNORE INTO contract_status (status) '
                           f'VALUES ("{status}")')


if __name__ == "__main__":
    create_contract_status_table()
    insert_statuses(CONTRACT_STATUSES)
    create_client_table()
    create_contract_table()
