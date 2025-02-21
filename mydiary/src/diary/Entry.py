from time import time, ctime


class Entry:
    def __init__(self, entry_id, title, body):
        self.__entry_id = entry_id
        self.__title = title
        self.__body = body
        self.__date_created = ctime(time())

    @property
    def entry_id(self):
        return self.__entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        self.__entry_id = entry_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def user_body(self):
        return self.__body

    @user_body.setter
    def user_body(self, user_body):
        self.__body = user_body

    @property
    def date_created(self):
        return self.__date_created

    @date_created.setter
    def date_created(self, date_created):
        self.__date_created = date_created
