#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import cgi
import psycopg2
from psycopg2 import Error


def print_header(user):
    print("Content-type: text/html")
    print("")
    print("""<html><head><title>Product</title>
            <script src = "user_search.js"></script>
            <link rel="stylesheet" href="shopping_cart.css"></head><body>
            <ul>
            <li style="background-color:rgb(223, 223, 223)"><a href="user_all.py?usr={}" style="color:red; font-family:Papyrus,Fantasy"">YMS</a></li>
            <li><a href="user_newreleases.py?usr={}">New Releases</a></li>
            <li>
            <div class="dropdown">
            <button class="dropbtn">Categories</button>
            <div class="dropdown-content">
             <a href="user_all.py?usr={}">All</a>
             <a href="user_clothes.py?usr={}">Clothes</a>
             <a href="user_glassware.py?usr={}">Glassware</a>
             <a href="user_bag.py?usr={}">Bag</a>
             <a href="user_accessories.py?usr={}">Accessories</a>
            </div>
            </div>
            </li>
            <li style="float:right"><a href="visitor.py">LogOut</a></li>
            <li style="float:right"><a href="account.py?usr={}">Account</a></li>
            <li style="float:right"><a href="user_cart.py?usr={}">Shopping cart</a></li>
            </ul>""".format(user, user, user, user, user, user, user, user, user, user))


def get_shopping_cart(usr):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Sb.19.23",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="yms")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        cursor.execute("""SELECT product_id, shopping_cart_id FROM Payment_Shopping_Cart WHERE have = %s""", [usr])
        row = cursor.fetchone()
        while row:
            cursor.execute("""SELECT product_name, p_size, price, product_type, product_image_file 
            FROM Product WHERE product_id = %s""", (row[0],))
            row2 = cursor.fetchone()
            if row2[3] == "Clothes" or "Glassware" or "Bag":
                print("""<div class="container">
                <div class="ShoppingCart">
                <div class="row">
                <div class="column"><img src="{}" style="width:50%"></div>
                <div class="column" style="text-align: left;">
                {} {} {}
                </div>
                <div class="column" style="text-align: left;">
                <button onclick="document.location='#'" >Remove From Cart</button> <button onclick="document.location='custamization.html'">Customize Product</button>
                </div>
                </div>""".format(row2[4], row2[0], row2[1], row2[2]))
            else:
                print("""<div class="container">
                <div class="ShoppingCart">
                <div class="row">
                <div class="column"><img src="{}" style="width:50%"></div>
                <div class="column" style="text-align: left;">
                {} {} {}
                </div>
                <div class="column" style="text-align: left;">
                <button onclick="document.location='#'" >Remove From Cart</button>
                </div>
                </div>""".format(row2[4], row2[0], row2[1], row2[2]))
            row = cursor.fetchone()
        print("</body></html>")
    except (Exception, Error) as error:
        print("Content-type: text/html")
        print("")
        print("""<html><head><title>Error</title></head><body>
         <p>Error while connecting to PostgreSQL</p>
         <p>{}</p>
         <p><a href = visitor.py>click to return main page</p></body>""", error)


if __name__ == '__main__':
    form = cgi.FieldStorage()
    usr = form["usr"].value
    print_header(usr)
    get_shopping_cart(usr)
