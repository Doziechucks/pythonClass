from unittest import TestCase
from src.bank.bank import Bank


class Banktest(TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_if_account_is_created(self):
        self.bank.create_account("firstname", "lastname", "password")
        actual = self.bank.get_number_of_account
        expected = 1
        self.assertEqual(actual, expected)

    def test_if_deposit_works(self):
        self.bank.create_account("firstname", "lastname", "password")
        self.bank.deposit(1, 2000)
        actual = self.bank.get_balance("password", 1)
        expected = 2000
        self.assertEqual(expected, actual)

    def test_if_withdraw_is_working(self):
        self.bank.create_account("firstname", "lastname", "password")
        self.bank.deposit(1, 2000)
        self.bank.withdraw(1, 800, "password")
        actual = self.bank.get_balance("password", 1)
        expected = 1200
        self.assertEqual(expected, actual)

    def test_if_transfer_works(self):
        self.bank.create_account("firstname", "lastname", "password")
        self.bank.create_account("first_name", "last_name", "pass_word")
        self.bank.deposit(2, 2000)
        self.bank.transfer(2, "pass_word", 1200, 1)
        self.assertEqual(800, self.bank.get_balance("pass_word", 2))
        self.assertEqual(1200, self.bank.get_balance("password", 1))
