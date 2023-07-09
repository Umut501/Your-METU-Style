#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import cgi
import psycopg2
from psycopg2 import Error
from database_objects import *
from user_html import *


def print_item(product, username):
    print(""" <img src="{}" """.format(product.get_img()))
    print("""
    <p></p>
    <div class="myClass2">
    <p>Product Name: {}</p>
    <p>Product Color: {}</p>
    <p>Product Size: {}</p>
    <p>Price: {}TL</p>
    <p>Stock: {}</p>
    <p>Description:</p>
    <p>{}</p>
    </div>
    """.format(product.get_name(), product.get_color(), product.get_size(), product.get_price(),
               product.get_quantity(), product.get_description()))
    print("""<p><button class="button"><a href="user_add_cart.py?id={}&usr={}" style="color:white">Add to cart</a></button></p>""".format(product.get_id(), username))


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


if __name__ == '__main__':
    form = cgi.FieldStorage()
    variable = form["usr"].value
    variable2 = form["id"].value
    print_product_page(variable)
    place_item(variable2, variable)
    print("""</body></html>""")
