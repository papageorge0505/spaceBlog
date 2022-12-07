import hashlib
import datetime


class User:
    __name: str
    __login: str
    __password: str
    __b_day: datetime.date.today()
    __telephone_number: str
    __status: str = "guest"  # user, admin, super admin
    __is_admin: False
    __is_authorized: False

    def __init__(self, name, login, password, b_day, is_admin):
        self.__name = name
        self.__login = login
        self.__password = password
        self.__b_day = b_day
        self.__is_admin = is_admin

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def b_day(self):
        return self.__b_day

    @b_day.setter
    def b_day(self, b_day):
        self.__b_day = b_day

    @property
    def telephone_number(self):
        return self.__telephone_number

    @telephone_number.setter
    def telephone_number(self, telephone_number):
        self.__telephone_number = telephone_number

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: bool):
        if status == True:
            self.__status = "Admin"

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, admin_status: bool):
        self.__is_admin = admin_status

    @property
    def is_authorized(self):
        return self.__is_authorized

    @is_authorized.setter
    def is_authorized(self, is_authorized: bool):
        self.__is_authorized = is_authorized

    @property
    def user(self):
        return print(f"{self.__name}, {self.__b_day}, {self.__telephone_number}, {self.__status}")


g = User("George", "papageorge", "0505", datetime.date(1991, 8, 22), True)


def user_age(name, b_day):
    today = datetime.date.today()
    age = today.year - b_day.year
    if today.month > b_day.month:
        print(f"{name} is {age} Y.O.")
    elif today.month < b_day.month:
        print(f"{name} is {age - 1} Y.O.")
    elif today.month == b_day.month:
        if today.day > b_day.day:
            print(f"{name} is {age} Y.O.")
        elif today.day < b_day.day:
            print(f"{name} is {age - 1} Y.O.")
        elif today.day == b_day.day:
            print(f"{name}!\nHappy {age} Y. O!")


# g.telephone_number("+380937177539")
# g.status(g.is_admin)
# g.user
user_age(g.name, g.b_day)
