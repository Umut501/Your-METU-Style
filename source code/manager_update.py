#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import cgi
import psycopg2
from psycopg2 import Error
from database_objects import *
from manager_forms import *
from datetime import datetime, timezone


def get_quantity(id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sb.19.23",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="yms")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("""SELECT quantity FROM Product WHERE product_id=%s""", (id,))
        row = cursor.fetchone()
        quantity = row[0]
        connection.commit()
        connection.close()
        return int(quantity)
    except (Exception, Error) as error:
        print("Content-type: text/html")
        print("")
        print("""<html><head><title>Error</title></head><body>
        <p>Error while connecting to PostgreSQL</p>
        <p>{}</p>
        <p><a href = manager_login.py>click to return main page</p></body>""".format(error))
        return 0


def update_table(id, variable):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sb.19.23",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="yms")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("""UPDATE Product SET quantity=%s WHERE product_id=%s""", (variable, id,))
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
    id = int(form["productid"].value)
    quantity = int(form["productQuantity"].value)
    new_quantity = get_quantity(id) + quantity
    if new_quantity > quantity:
        if update_table(id, new_quantity):
            print_forms("Update", "Stock updated successfully")
