#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
from database_objects import *
import cgi
import psycopg2
from psycopg2 import Error
from user_html import *


def registration(user_object):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sb.19.23",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="yms")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO User_Table (user_name, password, first_name, last_name, e_mail)
        VALUES(%s, crypt(%s, gen_salt('bf')), %s, %s, %s)""",
                       [user_object.get_username(), user_object.get_password(), user_object.get_first_name(),
                        user_object.get_last_name(), user_object.get_email()])
        cursor.execute("""INSERT INTO User_Phone_Number (phone_no, user_name) VALUES(%s, %s)""",
                       [user_object.get_phone_no(), user_object.get_username()])
        cursor.execute("""INSERT INTO User_Address (address, user_name) VALUES (%s, %s)""",
                       [user_object.get_address(), user_object.get_username()])
        connection.commit()
        connection.close()
        print("Content-type: text/html")
        print("")
        print("""<html><head><title>Success</title></head><body>
        <p>Your account created successfully</p>
        <p><a href = visitor_login.py>click to go to login page</p></body>""")
    except (Exception, Error) as error:
        print_invalid_register()
        print("""<p style="text-align: center">{}</p></body></html>""".format(error))


if __name__ == '__main__':
    form = cgi.FieldStorage()
    new_user = User(form["user_name"].value, form["password"].value, form["first_name"].value, form["last_name"].value,
                    form["e_mail"].value, form["phone_no"].value, form["address"].value)
    registration(new_user)
