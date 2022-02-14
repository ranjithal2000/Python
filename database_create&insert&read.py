import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
        conn=sqlite3.connect('sales.db')
        return conn
    except Error:
        print(Error)
def sql_table(conn):
    cursorObj = conn.cursor()
    cursorObj.execute("CREATE TABLE product(product_name char(50),product_id n(5))")
    cursorObj.executescript("""
    INSERT INTO product VALUES('Mobile', 20);
    INSERT INTO product VALUES('Watch', 18);
    INSERT INTO product VALUES('Laptop', 25);
    """)
    conn.commit()
    cursorObj.execute("SELECT product_name FROM product WHERE product_id <25")
    rows=cursorObj.fetchall()
    print("product details")
    for row in rows:
        print(row)
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")
