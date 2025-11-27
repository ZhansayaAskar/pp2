import psycopg2
import csv
from config import load_config


params = load_config()


def create_table():
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS phonebook (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        phone VARCHAR(20) NOT NULL UNIQUE
                    );
                """)
                conn.commit()
                print("Table was created successfully")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
def insert_csv(filename='contacts.csv'):
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                with open(filename, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        cur.execute(
                            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                            (row['name'], row['phone'])
                        )
                conn.commit()
                print("data from CSV successfully added")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        


def insert_console():
    name = input("Enter the contact name: ")
    phone = input("Enter your phone number: ")
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                    (name, phone)
                )
                conn.commit()
                print(f"contact {name} added")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        


def update_contact():
    contact_id = input("Введите ID контакта для обновления: ")
    new_name = input("New name): ")
    new_phone = input("New phone number: ")
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                if new_name:
                    cur.execute("UPDATE phonebook SET name=%s WHERE id=%s", (new_name, contact_id))
                if new_phone:
                    cur.execute("UPDATE phonebook SET phone=%s WHERE id=%s", (new_phone, contact_id))
                conn.commit()
                print(f"Contacts with ID={contact_id} updated")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        


def query_contacts():
    print("Filter for search:")
    print("1 - By name")
    print("2 - By number")
    print("3 - All contacts")
    option = input("Choose filter: ")
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                if option == "1":
                    value = input("Enter name: ")
                    cur.execute("SELECT * FROM phonebook WHERE name=%s", (value,))
                elif option == "2":
                    value = input("enter Phone: ")
                    cur.execute("SELECT * FROM phonebook WHERE phone=%s", (value,))
                else:
                    cur.execute("SELECT * FROM phonebook")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        


def delete_contact():
    value = input("Enter the name or phone number of the contact to be deleted:")
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM phonebook WHERE name=%s OR phone=%s", (value, value))
                conn.commit()
                print("Contact deleted")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        


if __name__ == '__main__':
    create_table()
    insert_csv()       
    insert_console()   
    update_contact()        
    query_contacts()        
    delete_contact()        