#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import cgi
import psycopg2
from psycopg2 import Error
from database_objects import *
from manager_forms import *
from datetime import datetime, timezone


def insert_table(p):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sb.19.23",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="yms")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO Product (product_description, price, quantity, product_name, 
        product_type, p_color, p_size, product_image_file)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""", (p.get_description(), float(p.get_price()),
                                                    float(p.get_quantity()), p.get_name(), p.get_type(),
                                                    p.get_color(), p.get_size(), p.get_img(),))
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
    dt = datetime.now(timezone.utc)
    new_product = Product(0, form["productDescription"].value, form["productPrice"].value,
                          form["productQuantity"].value,
                          form["productName"].value, dt, dt, form["productType"].value, form["productColor"].value,
                          form["productSize"].value,
                          form["product_image_file"].value, 0)
    if insert_table(new_product):
        print_forms("Insert", "Product added successfully")
