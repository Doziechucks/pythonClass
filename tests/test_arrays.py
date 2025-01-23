import unittest
from DSAclasswork.Arrays import Arrays;


class MyTestCase(unittest.TestCase):
    def test_if_arrays_can_add_element(self):
        array = Arrays(4)
        array.add("man")
        actual = array.get_size()
        expected = 4
        self.assertEqual(actual, expected)

    def test_if_array_can_hold_more_than_size(self):
        array = Arrays(1)
        array.add("man")
        array.add("woman")
        expected = 1
        actual = array.get_size()
        self.assertEqual(expected, actual)

    def test_if_array_can_add_more_than_an_item(self):
        array = Arrays(2)
        array.add("man")
        array.add("woman")
        expected = "['man', 'woman']"
        actual = array.toString()
        self.assertEqual(expected, actual)




