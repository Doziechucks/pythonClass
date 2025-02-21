class Account:
    def __init__(self, first_name, last_name, account_number, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = 0
        self.__account_number = account_number
        self.__password = password

    def password_check(self, input_password):
        if self.__password == input_password:
            return True
        else:
            return False

    def get_balance(self, input_password):
        if self.password_check(input_password):
            return self.__balance
        else:
            raise ValueError("Incorrect password")

    @property
    def get_first_name(self):
        return self.__first_name

    @get_first_name.setter
    def get_first_name(self, first_name):
        self.__first_name = first_name

    @property
    def get_last_name(self):
        return self.__last_name

    @get_last_name.setter
    def get_last_name(self, last_name):
        self.__first_name = last_name

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            raise ValueError("Invalid amount")

    def withdraw(self, amount, password):
        if self.password_check(password):
            if 0 < amount < self.__balance:
                self.__balance = self.__balance - amount
            else:
                raise ValueError("invalid amount")
        else:
            raise ValueError("Incorrect details")

    def change_pin(self, old_pin, new_pin):
        if self.password_check(old_pin):
            self.__password = new_pin
        else:
            raise ValueError("invalid credentials")





