from unittest import TestCase
from src.datastructure.myset import MySet


class MySetTest(TestCase):

    def test_if_elements_is_added_to_the_set(self):
        mySet = MySet()
        mySet.set_add(5)
        expected = mySet.get_list()
        actual = [5]
        self.assertEqual(expected, actual)

    def test_if_elements_can_regect_repeated_arguments(self):
        my_set = MySet()
        my_set.set_add(4)
        my_set.set_add(5)
        my_set.set_add(4)
        expected = my_set.get_list()
        actual = [4, 5]
        self.assertEqual(expected, actual)

    def test_if_set_can_be_compared(self):
        my_set_one = MySet()
        my_set_two = MySet()
        my_set_one.set_add("man")
        my_set_one.set_add(4)
        my_set_two.set_add(4)
        my_set_two.set_add("woman")
        actual = my_set_two.difference(my_set_one)
        expected = ["man"]







