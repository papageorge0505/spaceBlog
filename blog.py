class Blog:
    __blog_name: str
    __topic_list: []
    __user_blacklist: []

    @property
    def blog_name(self):
        return self.__blog_name

    @blog_name.setter
    def blog_name(self, blog_name: str):
        self.__blog_name = blog_name

    @property
    def topic_list(self):
        return self.__topic_list

    @topic_list.setter
    def topic_list(self, topic):
        self.__topic_list.add(topic)

    @property
    def user_blacklist(self):
        return self.__user_blacklist

    @user_blacklist.setter
    def user_blacklist(self, user):
        self.__user_blacklist.add(user)


class Topic(Blog):
    __topic_name: str
    __comments: []

    @property
    def topic_name(self):
        return self.__topic_name

    @topic_name.setter
    def topic_name(self, topic_name: str):
        self.__topic_name = topic_name

    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, comment):
        self.__comments.add(comment)


class Post(Topic):
    __description: str
    __post_body: str
    __author_name: str
    __banned_users: {}
    __likes_value: 0

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def post_body(self):
        return self.__post_body

    @post_body.setter
    def post_body(self, post_body: str):
        self.__post_body = post_body

    @property
    def author_name(self):
        return self.__author_name

    @author_name.setter
    def author_name(self, author_name: str):
        self.__author_name = author_name

    @property
    def banned_users(self):
        return self.__banned_users

    @banned_users.setter
    def banned_users(self, banned_users):
        self.__banned_users.add(banned_users)