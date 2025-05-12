from datetime import datetime


class Movie:
    def __init__(self, title):
        self.__title = title
        self.__upload_time = datetime.now()
        
    