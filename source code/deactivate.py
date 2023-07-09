#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import cgi
import psycopg2
from psycopg2 import Error
from database_objects import *
from user_html import *


def delete_user_info(usr):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sb.19.23",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="yms")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("""DELETE FROM Payment_Shopping_Cart WHERE have = %s""", [usr])
        cursor.execute("""DELETE FROM User_Phone_Number WHERE user_name = %s""", [usr])
        cursor.execute("""DELETE FROM User_Address WHERE user_name = %s""", [usr])
        cursor.execute("""DELETE FROM Credit_Debit_Card WHERE user_name = %s""", [usr])
        cursor.execute("""DELETE FROM User_Table WHERE user_name = %s""", [usr])
        connection.commit()
        connection.close()
        print("Content-type: text/html")
        print("")
        print("""
        <html><head><title>Error</title></head><body>
        <p>The account removed successfully</p>
        <p><a href = visitor.py>click to return main page</p></body>""")

    except (Exception, Error) as error:
        print("Content-type: text/html")
        print("")
        print("""<html><head><title>Error</title></head><body>
         <p>Error while connecting to PostgreSQL</p>
         <p><a href = visitor.py>click to return main page</p></body>""", error)


if __name__ == '__main__':
    form = cgi.FieldStorage()
    variable = form["usr"].value
    delete_user_info(variable)
