def print_product_page(username):
    print("Content-type: text/html")
    print("")
    print("""<html><head><title>Product</title>
    <script src = "user_search.js"></script>
    <link rel="stylesheet" type="text/css" href="user.css"></head><body>
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
    </ul>""".format(username, username, username, username, username, username, username, username, username,
                    username))


def print_user_page(username):
    print("Content-type: text/html")
    print("")
    print("""<html><head><title>UserHome</title>
    <script src = "user_search.js"></script>
    <link rel="stylesheet" type="text/css" href="user.css"></head><body>
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
    </ul>
    <p><form name="search_form" action="user_search.py" method="post" onsubmit="return validate();">
    <input type="text" id="search" name="search" placeholder="Search a product..">
    <input type="hidden" name="usr" value="{}">
    <input type="submit" value="Search">
    </form></p>""".format(username, username, username, username, username, username, username, username, username,
                          username))


def print_user_page_item(username, id, path, p_name, size, price):
    print("""
    <div class="gallery">
    <a target="_blank" href="user_product.py?usr={}&id={}">
    <img src="{}" width="600" height="400">
    </a>
    <div class="desc">
    <p>{}</p><p>{}</p><p>{} TL</p>
    </div>
    </div>""".format(username, id, path, p_name, size, price))


def print_user_page_footer():
    print("</body></html>")


def print_invalid_login_form():
    print("Content-type: text/html")
    print("")
    print("""<html><head><title>LogIn</title>
      <script src = "visitor_login.js"></script>
      <link rel="stylesheet" type="text/css" href="visitor_login.css"></head><body>
      <ul>
    <li style="background-color:rgb(223, 223, 223)"><a style="color:red; font-family:Papyrus,Fantasy" href="visitor.py">YMS</a></li>
    <li><a href="#categories">Categories</a></li>
    <li><a href="#bestsellers">BestSellers</a></li>
    <li><a href="#newreleases">New Releases</a></li>
    <li style="float:right"><a href="#register">SignUp</a></li>
    </ul>""")
    print("""
        <h2></h2>
        <div>
        <h2 style="color:black; text-align: center">LogIn</h2>
        <form name = "form_login" method="post" action= "user.py" onsubmit="return validate();">
        <label for="user_name">User name:</label><br>
        <input type="text" id="user_name" name="user_name"><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password">
        <p><input type="submit" value="LogIn" class="button button1"></p>
        </form>
        </div>""")
    print("""<p style="text-align: center">Your username or password is invalid!!!</p>""")
    print("</body></html>")


def print_invalid_register():
    print("Content-type: text/html")
    print("")
    print("""<html><head><title>LogIn</title>
      <script src = "visitor_login.js"></script>
      <link rel="stylesheet" type="text/css" href="visitor_register.css"></head><body>
      <ul>
    <li style="background-color:rgb(223, 223, 223)"><a style="color:red; font-family:Papyrus,Fantasy" href="visitor.py">YMS</a></li>
    <li><a href="#categories">Categories</a></li>
    <li><a href="#bestsellers">BestSellers</a></li>
    <li><a href="#newreleases">New Releases</a></li>
    <li style="float:right"><a href="visitor_login.py">LogIn</a></li>
    </ul>""")
    print("""
    <h2></h2>
    <div>
    <h2 style="color:black; text-align: center">Registration form</h2>
    <form name = "form_register" method="post" action= "user_register.py" onsubmit="return validate();">
    <label for="first_name">First name:</label><br>
    <input type="first_name" id="first_name" name="first_name">
    <label for="last_name">Surname:</label><br>
    <input type="last_name" id="last_name" name="last_name">
    <label for="user_name">User name:</label><br>
    <input type="text" id="user_name" name="user_name"><br>
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password">
    <label for="password2">Re-enter password:</label><br>
    <input type="password" id="password2" name="password2">
    <label for="e_mail">E-mail:</label><br>
    <input type="e_mail" id="e_mail" name="e_mail">
    <label for="phone_no">Phone number:</label><br>
    <input type="phone_no" id="phone_no" name="phone_no">
    <label for="address">Address:</label><br>
    <input type="address" id="address" name="address">
    <p><input type="submit" value="Register" class="button button1"></p>
    </form>
    </div>""")


def print_account(user):
    print("Content-type: text/html")
    print("")
    print("""<html><head><title>Product</title>
        <script src = "user_search.js"></script>
        <link rel="stylesheet" type="text/css" href="user.css"></head><body>
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
        </ul>""".format(user.get_username(), user.get_username(), user.get_username(), user.get_username(),
                        user.get_username(), user.get_username(), user.get_username(), user.get_username(),
                        user.get_username(),
                        user.get_username()))
    print("""
    <div class="myClass">
    <p>User name:{}</p>
    <p>Firstname:{}</p>
    <p>Lastname:{}</p>
    <p>Email:{}</p>
    <p>Phone Number:{}</p>
    <p>Address:{}</p></div>""".format(user.get_username(), user.get_first_name(), user.get_last_name(),
                                      user.get_email(), user.get_phone_no(), user.get_address()))
    print(
        """<p><button class="button"><a href="deactivate.py?usr={}" style="color:white">Deactivate the account</a></button></p>""".format(
            user.get_username()))
    print("</body></html>")
