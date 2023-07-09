#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe

def print_header(title):
    print("Content-type: text/html")
    print("")
    print("""<html><head><title>{}</title><link rel="stylesheet" type="text/css" href="user.css"></head><body>
    <ul>
  <li style="background-color:rgb(223, 223, 223)"><a style="color:red; font-family:Papyrus,Fantasy" href="visitor.py">YMS</a></li>
  <li><a href="#categories">Categories</a></li>
  <li><a href="#bestsellers">BestSellers</a></li>
  <li><a href="#newreleases">New Releases</a></li>
  <li style="float:right"><a href="visitor.py">LogOut</a></li>
  <p><form><input type="text" name="search" placeholder="Search a product..">
  <input type="submit" value="Search">
  </form></p>
  </ul>""".format(title))


def print_footer():
    print("</body></html>")


if __name__ == '__main__':
    print_header("Homepage")
    print_footer()
