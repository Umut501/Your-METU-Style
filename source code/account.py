#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import cgi
import psycopg2
from psycopg2 import Error
from database_objects import *
from user_html import *


def get_user_info(usr):
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
        print_account(user)

    except (Exception, Error) as error:
        print("Content-type: text/html")
        print("")
        print("""<html><head><title>Error</title></head><body>
         <p>Error while connecting to PostgreSQL</p>
         <p><a href = visitor.py>click to return main page</p></body>""", error)


if __name__ == '__main__':
    form = cgi.FieldStorage()
    username = form["usr"].value
    get_user_info(username)
