#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys


def print_header(title):
    print("Content-type: text/html")
    print("")
    print("""<html><head><title>{}</title>
    <script src = "visitor_register.js"></script>
    <link rel="stylesheet" type="text/css" href="visitor_register.css"></head><body>
    <ul>
  <li style="background-color:rgb(223, 223, 223)"><a style="color:red; font-family:Papyrus,Fantasy" href="visitor.py">YMS</a></li>
  <li style="float:right"><a href="visitor_login.py">LogIn</a></li>
  </ul>""".format(title))


def print_form():
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


def print_footer():
    print("</body></html>")


if __name__ == '__main__':
    print_header("Register")
    print_form()
    print_footer()
