#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import cgi
import random

import psycopg2
from psycopg2 import Error
from database_objects import *
from user_html import *
from user_product import print_item


def get_product(id):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sb.19.23",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="yms")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("""SELECT product_id, product_description, price, quantity, product_name, 
        created_at, updated_at, product_type, p_color, p_size, product_image_file, total_price FROM Product
        WHERE product_id = {}""".format(id))
        row = cursor.fetchone()
        new_product = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                              row[9], row[10], row[11])
        connection.commit()
        connection.close()
        return new_product

    except (Exception, Error) as error:
        print("""<p>Error while connecting to PostgreSQL:{}</p>
               <p><a href = visitor.py>click to return to the main page</p></body>""".format(error))


def get_user(usr):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sb.19.23",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="yms")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM User_Table WHERE user_name = %s""", [usr])
        row = cursor.fetchone()
        user = row[0]
        psw = row[1]
        first = row[2]
        last = row[3]
        mail = row[4]
        connection.commit()
        cursor.execute("""SELECT * FROM User_Phone_Number WHERE user_name = %s""", [usr])
        row = cursor.fetchone()
        p_no = row[0]
        connection.commit()
        cursor.execute("""SELECT * FROM User_Address WHERE user_name = %s""", [usr])
        row = cursor.fetchone()
        a_no = row[0]
        connection.commit()
        connection.close()
        user = User(user, psw, first, last, mail, p_no, a_no)
        return user
    except (Exception, Error) as error:
        print("Content-type: text/html")
        print("")
        print("""<html><head><title>Error</title></head><body>
            <p>Error while connecting to PostgreSQL</p>
            <p><a href = visitor.py>click to return main page</p></body>""", error)


def place_item(p_id, username):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sb.19.23",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="yms")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("""SELECT product_id, product_description, price, quantity, product_name, 
        created_at, updated_at, product_type, p_color, p_size, product_image_file, total_price FROM Product
        WHERE product_id = {}""".format(p_id))
        row = cursor.fetchone()
        while row:
            new_product = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                  row[9], row[10], row[11])
            print_item(new_product, username)
            row = cursor.fetchone()
        connection.commit()
        connection.close()
    except (Exception, Error) as error:
        print("""<p>Error while connecting to PostgreSQL:{}</p>
               <p><a href = visitor.py>click to return to the main page</p></body>""".format(error))


def add_cart(usr, i_d, object_user, object_product):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sb.19.23",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="yms")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Payment_Shopping_Cart (product_id, payment_amount, payment_address, number_of_products, have) VALUES(%s, %s, %s, %s, %s)""",
            [i_d, float(object_product.get_price()), object_user.get_address(), 1, usr])
        connection.commit()
        connection.close()
        print_product_page(usr)
        place_item(object_product.get_id(), usr)
        print("""Item added to shopping cart</body></html>""")
    except (Exception, Error) as error:
        print("Content-type: text/html")
        print("")
        print("""<html><head><title>Error</title></head><body>
         <p>Error while connecting to PostgreSQL</p>
         <p>{}</p>
         <p><a href = visitor.py>click to return main page</p></body>""", error)


if __name__ == '__main__':
    form = cgi.FieldStorage()
    username = form["usr"].value
    p_id = int(form["id"].value)
    user = get_user(username)
    product = get_product(p_id)
    add_cart(username, p_id, user, product)
