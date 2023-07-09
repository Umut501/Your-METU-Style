#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import psycopg2
from psycopg2 import Error
from database_objects import *
from visitor import print_header, print_all_items, print_footer


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
        WHERE quantity > 0
        ORDER BY created_at DESC;""")
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


if __name__ == '__main__':
    print_header("New Releases")
    place_items()
    print_footer()