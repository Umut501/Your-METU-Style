#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import psycopg2
from psycopg2 import Error
from database_objects import *
from manager_forms import *
from datetime import datetime, timezone


def header():
    print("Content-type: text/html")
    print("")
    print("""<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manager Page</title>
    <link rel="stylesheet" href="style.css">

    </head>
    <body class="bg">

    <ul>
      <li style="background-color:rgb(223, 223, 223)"><a style="color:red; font-family:Papyrus,Fantasy">YMS</a></li>
      <li style="float:right"><a href="manager_login.py">LogOut</a></li>
        <li class="dropdown">
            <a href="javascript:void(0)" class="dropbtn">PRODUCTS</a>
            <div class="dropdown-content">
              <a href="manager_product.py">MANAGE PRODUCTS</a>
              <a href="manager_display.py">DISPLAY PRODUCTS</a>
            </div>
          </li>
        <li>
          <a href="#">CUSTOMIZATION APPROVAL</a>
        </li>
      </ul>
      """)


def print_products():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sb.19.23",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="yms")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("""SELECT  product_id, product_description, price, quantity, product_name, 
        created_at, updated_at, product_type, p_color, p_size, product_image_file, total_price FROM Product""")
        row = cursor.fetchone()
        header()
        while row:
            print("""<div class="container2"><p><img src="{}" width="150" height="180"></p>
            <p>Id: {}</p> <p>Description: {}</p> <p>Price: {}</p> <p>Quantity: {}</p> <p>Name: {}</p> <p>Created Date: {}</p>
            <p>Last Update: {}</p> <p>Type: {}</p> <p>Color: {}</p> <p>Size: {}</p></div><p></p>
            """.format(row[10], row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            row = cursor.fetchone()
        print("""</body></html>""")
        connection.commit()
        connection.close()
    except (Exception, Error) as error:
        print("Content-type: text/html")
        print("")
        print("""<html><head><title>Error</title></head><body>
        <p>Error while connecting to PostgreSQL</p>
        <p>{}</p>
        <p><a href = manager_login.py>click to return main page</p></body>""".format(error))


if __name__ == '__main__':
    print_products()
