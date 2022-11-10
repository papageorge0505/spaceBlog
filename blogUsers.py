import base64


class User:
    __name: str
    __password: base64
    __age: int = 18
    __status: str = "user"  # user, admin, superadmin
    __is_admin: bool = False
    __is_authorized: bool = False

    def __init__(self, name, password, age):
        self.__name = name
        self.__password = password
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, admin_status: bool):
        self.__is_admin = admin_status


class SuperAdmin(User):
    def get_all_user_data(self, user):
        print(f"All user data\n"
              f"Name: {user.__name}\n"
              f"Password: {base64.encode(user.__password)}\n"
              f"Age: {user.__age}\n"
              f"Status: {user.__status}\n"
              f"Is admin: {user.__is_admin}\n"
              f"Is authorized: {user.__is_authorized}")

    def change_admin_status(self, db, user_name: str, status: bool):
        x = False
        for i in db.registered_user_db:
            if i.name == user_name:
                x = True
                if status:  # if status var = True
                    i.status = "Admin"
                    i.is_admin = status
                    print(f"{i.name}'s admin status changed to: {i.status}")
                else:
                    i.status = "User"
                    i.is_admin = status
                    print(f"{i.name}'s admin status changed to: {i.status}")

        if not x:
            print(f"No user with name {user_name}.")


e = SuperAdmin("George", "0505", 20)

e.status = "SuperAdmin"
