from src.bank.account import Account


class Bank:
    def __init__(self):
        self.__account_number = 1
        self.__bank_list: list[Account] = []

    def create_account(self, firstname, lastname, password):
        account = Account(firstname, lastname, self.__account_number, password)
        if password == "":
            raise ValueError("Invalid password Input")
        if firstname == "":
            raise ValueError("Invalid firstname Input")
        if lastname == "":
            raise ValueError("Invalid lastname Input")
        self.__bank_list.append(account)
        self.__account_number += 1

    def find_account(self, account_number):
        for account in self.__bank_list:
            if account.account_number == account_number:
                return self.__bank_list.index(account)
        return -1

    def deposit(self, account_number, amount):
        index = self.find_account(account_number)
        if index == -1:
            raise ValueError("Invalid account number")
        else:
            self.__bank_list[index].deposit(amount)

    def get_balance(self, password, account_number):
        index = self.find_account(account_number)
        if index == -1:
            raise ValueError("Invalid account number")
        else:
            return self.__bank_list[index].get_balance(password)

    def withdraw(self, account_number, amount, password):
        index = self.find_account(account_number)
        if index == -1:
            raise ValueError("Invalid account number")
        else:
            self.__bank_list[index].withdraw(amount, password)

    def transfer(self, withdraw_account, withdraw_password, amount, deposit_account):
        index_one = self.find_account(withdraw_account)
        index_two = self.find_account(deposit_account)
        if index_one == -1:
            raise ValueError("invalid account detail")
        elif index_two == -1:
            raise ValueError("no account with account number input")
        else:
            self.__bank_list[index_one].withdraw(amount, withdraw_password)
            self.__bank_list[index_two].deposit(amount)

    @property
    def get_number_of_account(self):
        return len(self.__bank_list)





