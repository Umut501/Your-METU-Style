#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import cgi
import psycopg2
from psycopg2 import Error
from manager_forms import print_forms, print_invalid_manager_form


class LogIn:

    def __init__(self, eml, pwd):
        self.__e_mail = eml
        self.__password = pwd

    def e_mail(self):
        return self.__e_mail

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
            cursor.execute("""SELECT * FROM Manager WHERE e_mail = %s 
            AND password = crypt(%s, password)""", [self.__e_mail, self.__password])
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


if __name__ == '__main__':
    form = cgi.FieldStorage()
    new_manager = LogIn(form["e_mail"].value, form["password"].value)
    if new_manager.check_login() == 1:
        print_forms("Management System", " ")
    else:
        print_invalid_manager_form()

