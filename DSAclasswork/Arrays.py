from sqlalchemy import null


class Arrays:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.array = []

    def add(self, value):
        if self.size < self.capacity:
            self.size += 1
            self.array += [value]
        else:
            raise ValueError


    def get_size(self):
        return self.size

    def toString(self):
        words = "["
        for element in range(len(self.array ) - 1):
            words += "\'"
            words += self.array[element]
            words += "\', \'"
        words += self.array[len(self.array ) - 1]
        words += "\'"
        words += "]"
        return words

    def remove(self, word):
        for number in range(len(self.array) - 1):
            if self.array[number] == word:
                self.array[number] = "null"
        return self.array




    def set(self, index, word):
        for number in range(len(self.array) - 1):
            if number == index:
                self.array[number] = word
        return self.array
