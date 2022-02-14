#insert and count rows
import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
        conn = sqlite3.connect('Sales.db')
        return conn
    except Error:
        print(Error)
def sql_table(conn):
    cursorObj = conn.cursor()
    cursor = cursorObj.execute('select * from product;')
    print(len(cursor.fetchall()))
    cursorObj.executescript("""
    INSERT INTO product VALUES('Bag', 42);
    INSERT INTO product VALUES('Chair', 38);
    """)
    conn.commit()
    print("\nNumber of records after inserting rows:")
    cursor = cursorObj.execute('select * from product;')
    print(len(cursor.fetchall()))
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")
