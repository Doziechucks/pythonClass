from unittest import TestCase
from src.diary.diaries import Diaries

class TestDiaries(TestCase):
    def setUp(self):
        self.diaries = Diaries()

    def test_if_diary_is_created(self):
        self.diaries.add_user("dozie", "money")
        self.assertEqual(1, self.diaries.get_diary_size())

    def test_to_find_user_by_user_name(self):
        self.diaries.add_user("dozie", "money")
        self.diaries.add_user("ifeanyi", "cyriacus")
        actual = self.diaries.find_diary_by_username("dozie").validate_password("money")
        expected = True
        self.assertEqual(actual, expected)

    def test_if_diary_is_deleted(self):
        self.diaries.add_user("dozie", "money")
        self.assertEqual(1, self.diaries.get_diary_size())
        self.diaries.delete_user("dozie", "money")
        self.assertEqual(0, self.diaries.get_diary_size())





