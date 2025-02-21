from unittest import TestCase
from src.bank.account import Account


class TestAccount(TestCase):
    def setUp(self):
        self.account = Account("first_name", "last_name", 1, "Password")

    def test_if_balance_is_returned(self):
        actual = self.account.get_balance("Password")
        expected = 0
        self.assertEqual(actual, expected)

    def test_if_first_name_is_returned(self):
        actual = self.account.get_first_name
        expected = "first_name"
        self.assertEqual(actual, expected)

    def test_if_deposit_works(self):
        self.account.deposit(500)
        actual = self.account.get_balance("Password")
        expected = 500
        self.assertEqual(actual, expected)

    def test_if_test_if_withdrawals_work(self):
        self.account.deposit(5000)
        actual = self.account.get_balance("Password")
        self.assertEqual(actual, 5000)
        self.account.withdraw(4500, "Password")
        result = self.account.get_balance("Password")
        self.assertEqual(result, 500)

    def test_if_password_can_be_changed(self):
        self.account.change_pin("Password", "money")
        actual = self.account.password_check("money")
        self.assertEqual(actual, True)



