#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import psycopg2
from psycopg2 import Error
from database_objects import *


def print_header(title):
    print("Content-type: text/html")
    print("")
    print("""<html><head><title>{}</title><link rel="stylesheet" type="text/css" href="visitor.css"></head><body>
  <ul>
  <li style="background-color:rgb(223, 223, 223)"><a style="color:red; font-family:Papyrus,Fantasy" href="visitor.py">YMS</a></li>
  <li><a href="visitor_newreleases.py">New Releases</a></li>
  <li>
  <div class="dropdown">
  <button class="dropbtn">Categories</button>
  <div class="dropdown-content">
  <a href="visitor.py">All</a>
  <a href="visitor_clothes.py">Clothes</a>
  <a href="visitor_glassware.py">Glassware</a>
  <a href="visitor_bag.py">Bag</a>
  <a href="visitor_accessories.py">Accessories</a>
  </div>
  </div>
  </li>
  <li style="float:right"><a href="visitor_register.py">SignUp</a></li>
  <li style="float:right"><a href="visitor_login.py">LogIn</a></li>
  <li style="float:right"><a href="manager_login.py">Manager</a></li>
  </ul>""".format(title))


def print_all_items(id, path, p_name, size, price):
    print("""
        <div class="gallery">
        <a target="_blank" href="visitor_product.py?id={}">
        <img src="{}" width="600" height="400">
        </a>
        <div class="desc">
        <p>{}</p><p>{}</p><p>{} TL</p>
        </div>
        </div>""".format(id, path, p_name, size, price))


def place_items():
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
            print_all_items(new_product.get_id(), new_product.get_img(), new_product.get_name(),
                            new_product.get_size(), new_product.get_price())
            row = cursor.fetchone()
        connection.commit()
        connection.close()
    except (Exception, Error) as error:
        print("""<p>Error while connecting to PostgreSQL:{}</p>
               <p><a href = visitor.py>click to return to the main page</p></body>""".format(error))


def print_footer():
    print("</body></html>")


if __name__ == '__main__':
    print_header("Visitor")
    place_items()
    print_footer()
