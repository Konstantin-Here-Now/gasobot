import datetime
import sqlite3

from exceptions import NotFoundInDatabase


def view_contract(contract_number: str) -> dict[str, str]:
    with sqlite3.connect("../database.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM contract '
                       f'WHERE contract_number="{contract_number}"')
        contract = cursor.fetchone()
        if contract:
            contract_info = {
                "contract_number": contract[1],
                "status": contract[2],
                "contract_client": contract[3],
                "sign_date": contract[4],
                "expire_date": contract[5]
            }
            return contract_info
        else:
            raise NotFoundInDatabase


def add_contact(contract_number, status, contract_client, sign_date, expire_date) -> None:
    with sqlite3.connect("../database.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute(
            f'INSERT OR IGNORE INTO contract (contract_number, status, contact_client, sign_date, expire_date)'
            f'VALUES ("{contract_number}", "{status}", "{contract_client}", "{sign_date}", "{expire_date}")')


def change_contract():
    pass


def add_client(client_name) -> None:
    with sqlite3.connect("../database.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT OR IGNORE INTO client (client_name) '
                       f'VALUES ("{client_name}")')


if __name__ == '__main__':
    # add_contact("2341-63", "Active", "Rosneft", datetime.date.today().isoformat(),
    #             datetime.date(2023, 10, 20).isoformat())
    contract_ = view_contract("2341-63")
    print(contract_)
