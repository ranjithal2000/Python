#update
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
    print("Agent details:")
    for row in rows:
        print(row)
    print("\nUpdate product_id 25 to 55 where product_name is Laptop")
    sql_update_query = """Update product set product_id = 65 where product_name = 'Mobile'"""
    cursorObj.execute(sql_update_query)
    conn.commit()
    print("Record Updated successfully ")
    cursorObj.execute("SELECT * FROM product")
    rows = cursorObj.fetchall()
    print("\nAfter updating Agent details:")
    for row in rows:
        print(row)
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
  sqllite_conn.close()
  print("\nThe SQLite connection is closed.")
