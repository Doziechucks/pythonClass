from diary.diary import Diary


class Diaries:
    def __init__(self):
        self.__diary_list: list[Diary] = []

    def add_user(self, username, password):
        diary = Diary(username, password, )
        self.__diary_list.append(diary)

    def find_diary_by_username(self, username):
        for diary in self.__diary_list:
            if diary.get_username == username:
                return diary
            else:
                return None

    def delete_user(self, username, password):
        diary = self.find_diary_by_username(username)
        if diary is not None and diary.validate_password(password) == True:
            return self.__diary_list.remove(diary)
        else:
            return "diary not found"

    def get_diary_size(self):
        return len(self.__diary_list)



