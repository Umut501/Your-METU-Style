#!C:\Users\sergu\AppData\Local\Programs\Python\Python310\python.exe
import sys
import cgi
import psycopg2
from psycopg2 import Error
from database_objects import *
from manager_forms import *

if __name__ == '__main__':
    print_forms("Manager", " ")
