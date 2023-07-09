#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import cgi
import psycopg2
from psycopg2 import Error
from database_objects import *
from manager_forms import *
from datetime import datetime, timezone


def delete_table(id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sb.19.23",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="yms")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("""DELETE FROM Product WHERE product_id=%s""", (id,))
        connection.commit()
        connection.close()
        return 1
    except (Exception, Error) as error:
        print("Content-type: text/html")
        print("")
        print("""<html><head><title>Error</title></head><body>
        <p>Error while connecting to PostgreSQL</p>
        <p>{}</p>
        <p><a href = manager_login.py>click to return main page</p></body>""".format(error))
        return 0


if __name__ == '__main__':
    form = cgi.FieldStorage()
    variable = int(form["productid"].value)
    if delete_table(variable):
        print_forms("Delete", "Product deleted successfully")
