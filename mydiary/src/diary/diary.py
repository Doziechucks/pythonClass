from diary.Entry import Entry


class Diary:
    def __init__(self, username, password) -> None:
        self.__username = username
        self.__password = password
        self.__is_locked: bool = True
        self.__entry_list: list[Entry] = []
        self.__entry_id = 0

    def unlock_diary(self):
        self.__is_locked = False

    def lock_diary(self):
        self.__is_locked = True

    def is_locked(self):
        return self.__is_locked

    def create_entry(self, title, body):
        entry = Entry(self.__entry_id + 1, title, body)
        self.__entry_list.append(entry)

    def find_entry_by_id(self, the_entry_id):
        for entry in self.__entry_list:
            if entry.entry_id == the_entry_id:
                return entry
            else:
                return None

    def delete_entry(self, the_entry_id):
        entry = self.find_entry_by_id(the_entry_id)
        if entry is not None:
            self.__entry_list.remove(entry)
        else:
            return "Entry not found"

    def update_entry(self, the_entry_id, new_title, update):
        entry = self.find_entry_by_id(the_entry_id)
        if entry is not None:
            entry.title = new_title
            entry.user_body = entry.user_body + "\n" + update

    @property
    def get_username(self):
        return self.__username

    @get_username.setter
    def get_username(self, username):
        self.__username = username

    def validate_password(self, password):
        if self.__password == password:
            return True
        else:
            return False

    @property
    def password(self, password):
        self.__password = password

    def validate_password(self, password):
        if self.__password == password:
            return True
        else:
            return False

    def get_size(self):
        return len(self.__entry_list)


