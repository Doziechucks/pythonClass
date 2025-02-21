from unittest import TestCase
from src.diary.diary import Diary


class TestDiary(TestCase):
    def setUp(self):
        self.diary = Diary("Dozie", "money")

    def test_if_diary_can_be_locked_and_unlocked(self):
        self.assertEqual(self.diary.is_locked(), True)
        self.diary.unlock_diary()
        self.assertEqual(self.diary.is_locked(), False)
        self.diary.lock_diary()
        self.assertEqual(self.diary.is_locked(), True)

    def test_if_entry_is_created(self):
        self.diary.create_entry("my title", "my money")
        expected = self.diary.find_entry_by_id(1).title
        actual = "my title"
        self.assertEqual(actual, expected)

    def test_if_entry_can_be_deleted(self):
        self.diary.create_entry("my title", "my money")
        self.diary.create_entry("dozie", "money money")
        self.assertEqual(2, self.diary.get_size())
        self.diary.delete_entry(1)
        actual = self.diary.get_size()
        expected = 1
        self.assertEqual(actual, expected)

    def test_if_entry_is_updated(self):
        self.diary.create_entry("my title", "my money")
        self.diary.update_entry(1, "I am titled", "Dozie Money")
        self.assertEqual(self.diary.find_entry_by_id(1).title, "I am titled")
        self.assertEqual(self.diary.find_entry_by_id(1).user_body, "my money\nDozie Money")
