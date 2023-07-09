#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import cgi
import psycopg2
from psycopg2 import Error

from database_objects import *
from user_html import *


class LogIn:
    def __init__(self, usr, pwd):
        self.__username = usr
        self.__password = pwd

    def get_user(self):
        return self.__username

    def get_password(self):
        return self.__password

    def check_login(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="Sb.19.23",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="yms")
            # Create a cursor to perform database operations
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM User_Table WHERE user_name = %s 
            AND password = crypt(%s, password)""", [self.__username, self.__password])
            row = cursor.fetchall()
            if not row:
                connection.commit()
                connection.close()
                return 0
            else:
                connection.commit()
                connection.close()
                return 1

        except (Exception, Error) as error:
            print("Content-type: text/html")
            print("")
            print("""<html><head><title>Error</title></head><body>
            <p>Error while connecting to PostgreSQL</p>
            <p><a href = visitor.py>click to return main page</p></body>""", error)
            return 0


def place_items(username):
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
         WHERE quantity > 0""")
        row = cursor.fetchone()
        while row:
            new_product = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                  row[9], row[10], row[11])
            print_user_page_item(username, new_product.get_id(), new_product.get_img(), new_product.get_name(),
                                 new_product.get_size(), new_product.get_price())
            row = cursor.fetchone()
        connection.commit()
        connection.close()
    except (Exception, Error) as error:
        print("""<p>Error while connecting to PostgreSQL:{}</p>
               <p><a href = visitor.py>click to return to the main page</p></body>""".format(error))


if __name__ == '__main__':
    form = cgi.FieldStorage()
    new_user = LogIn(form["user_name"].value, form["password"].value)
    if new_user.check_login() == 1:
        print_user_page(new_user.get_user())
        place_items(new_user.get_user())
        print_user_page_footer()
    else:
        print_invalid_login_form()
