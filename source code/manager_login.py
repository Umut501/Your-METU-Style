#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe

def print_header(title):
    print("Content-type: text/html")
    print("")
    print("""<html><head><title>{}</title>
    <script src = "manager_login.js"></script>
    <link rel="stylesheet" type="text/css" href="manager_login.css"></head><body>
    <ul>
    <li style="background-color:rgb(223, 223, 223)"><a style="color:red; font-family:Papyrus,Fantasy" href="visitor.py">YMS</a></li>
    </ul>""".format(title))


def print_form():
    print("""
    <h2></h2>
    <div>
    <h2 style="color:black; text-align: center">Management System</h2>
    <form name = "manager_login" method="post" action= "manager.py" onsubmit="return validate();">
    <label for="e_mail">E-mail:</label><br>
    <input type="text" id="e_mail" name="e_mail">
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password">
    <p><input type="submit" value="LogIn" class="button button1"></p>
    </form>
    </div>""")


def print_footer():
    print("</body></html>")


if __name__ == '__main__':
    print_header("Management System")
    print_form()
    print_footer()
