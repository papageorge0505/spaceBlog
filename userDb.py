class RegisteredUserDb:
    __reg_user_db: set

    @property
    def registered_user_db(self):
        return self.__reg_user_db

    @registered_user_db.setter
    def registered_user_db(self, user):
        self.__reg_user_db.add(user)

    def get_all_users(self):
        for user in self.__reg_user_db:
            print(f"All users:\n{user}")

    # TODO show user to delete and check if the deletion is successfully complete or not
    def delete_user(self, user):
        self.__reg_user_db.discard(user)