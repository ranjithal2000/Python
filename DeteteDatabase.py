#delete
import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
      conn = sqlite3.connect('Sales.db')
      return conn
    except Error:
      print(Error)
def sql_table(conn):
    cursorObj = conn.cursor()  #Sales.db
    #Current records in salesman table
    cursorObj.execute("SELECT * FROM product")
    rows = cursorObj.fetchall()
    print("Product details:")
    for row in rows:
        print(row)
    print("\nDlete product where name is 'Mobile':")
    sql_delete_query = """DELETE FROM product WHERE product_id = 65"""
    cursorObj.execute(sql_delete_query)
    conn.commit()
    print("Record Deleted successfully ")
    cursorObj.execute("SELECT * FROM product")
    rows = cursorObj.fetchall()
    print("\nAfter deleting product details:")
    for row in rows:
        print(row)
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
  sqllite_conn.close()
  print("\nThe SQLite connection is closed.")
