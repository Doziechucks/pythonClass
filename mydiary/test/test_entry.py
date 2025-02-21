from unittest import TestCase
from src.diary.Entry import Entry
from time import time, ctime


class TestEntry(TestCase):

    def setUp(self):
        self.entry = Entry(1, "my title", "the body")

    def test_if_created_date_is_returned(self):
        expected = ctime(time())
        actual = self.entry.date_created
        self.assertEqual(expected, actual)

    def test_if_title_is_returned(self):
        actual = self.entry.user_body
        expected = "the body"
        self.assertEqual(actual, expected)
