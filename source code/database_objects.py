# parent class
class Person:
    def __init__(self, fname, lname, email, psw, phone, adr):
        # protected class members
        self._first_name = fname
        self._last_name = lname
        self._e_mail = email
        self._password = psw
        self._phone_no = phone
        self._address = adr

    def get_password(self):
        return self._password

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._e_mail

    def get_address(self):
        return self._address

    def get_phone_no(self):
        return self._phone_no


# child class for Person
class User(Person):
    def __init__(self, usr, psw, fname, lname, email, phone, adr):
        super().__init__(fname, lname, email, psw, phone, adr)
        self.__user_name = usr

    def get_username(self):
        return self.__user_name


class Manager(Person):
    def __init__(self, id, fname, lname, email, psw, phone, adr):
        super().__init__(fname, lname, email, psw, phone, adr)
        self.__manager_id = id

    def get_manager_id(self):
        return self.__manager_id


class Product:
    def __init__(self, id, desc, price, quant, name, cr, up, typ, color, size, img, total):
        self.__product_id = id
        self.__product_description = desc
        self.__product_price = price
        self.__product_quantity = quant
        self.__product_name = name
        self.__product_create_date = cr
        self.__product_update_date = up
        self.__product_type = typ
        self.__product_color = color
        self.__product_size = size
        self.__product_image = img
        self.__product_total_price = total

    def get_id(self):
        return self.__product_id

    def get_img(self):
        return self.__product_image

    def get_name(self):
        return self.__product_name

    def get_price(self):
        return self.__product_price

    def get_size(self):
        return self.__product_size

    def get_color(self):
        return self.__product_color

    def get_quantity(self):
        return self.__product_quantity

    def get_description(self):
        return self.__product_description

    def get_type(self):
        return self.__product_type
