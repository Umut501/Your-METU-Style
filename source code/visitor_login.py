#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe

def print_header(title):
    print("Content-type: text/html")
    print("")
    print("""<html><head><title>{}</title>
    <script src = "visitor_login.js"></script>
    <link rel="stylesheet" type="text/css" href="visitor_login.css"></head><body>
    <ul>
  <li style="background-color:rgb(223, 223, 223)"><a style="color:red; font-family:Papyrus,Fantasy" href="visitor.py">YMS</a></li>
  <li style="float:right"><a href="visitor_register.py">SignUp</a></li>
  </ul>""".format(title))


def print_form():
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


def print_footer():
    print("</body></html>")


if __name__ == '__main__':

    print_header("LogIn")
    print_form()
    print_footer()
