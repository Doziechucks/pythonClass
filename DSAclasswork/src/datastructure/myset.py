class MySet:
    def __init__(self):
        self.__mylist = []

    def get_list(self):
        return self.__mylist

    def set_add(self, element):
        if not self.__mylist.__contains__(element):
            self.__mylist.append(element)

    def difference(self, item: object) -> object:
        new_set = []
        for element in self.__mylist:
            if item.__contains__(element):
                continue
            new_set.append(element)
        return new_set
