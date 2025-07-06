from datetime import datetime


class Movie:
    def __init__(self, title):
        self.__title = title
        self.__upload_time = datetime.now().replace(microsecond=0)


    @property
    def get_title(self):
        return self.__title

    @get_title.setter
    def get_title(self, title):
        self.__title = title

    def get_upload_time(self):
        return self.__upload_time




        
    