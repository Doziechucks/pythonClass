class Arrays:
    def __init__(self, size):
        self.size = 0
        self.capacity = size
        self.array = []

    def add(self, value):
        if self.size != self.capacity:
            self.size += 1
            return self.array.append(value)


    def get_size(self):
        return self.capacity

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

