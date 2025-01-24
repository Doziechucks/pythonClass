import unittest
from DSAclasswork.Arrays import Arrays;


class MyTestCase(unittest.TestCase):
    def test_if_arrays_can_add_element(self):
        array = Arrays(4)
        array.add("man")
        array.add("boy")
        array.add("gentleman")
        actual = array.get_size()
        expected = 3
        self.assertEqual(actual, expected)

    def test_if_array_can_not_hold_more_than_its_capacity(self):
        array = Arrays(1)
        array.add("man")
        self.assertRaises(ValueError, array.add, "woman")
        self.assertEqual(1, array.get_size())

    def test_if_array_can_add_more_than_an_item(self):
        array = Arrays(2)
        array.add("man")
        array.add("woman")
        expected = "['man', 'woman']"
        actual = array.toString()
        self.assertEqual(actual, expected)

    def test_if_list_can_remove(self):
        array = Arrays(2)
        array.add("man")
        array.add("woman")
        expected = ['null', 'woman']
        actual = array.remove("man")
        self.assertEqual(expected, actual)



    def test_if_list_can_set_element(self):
        array = Arrays(3)
        array.add("man")
        array.add("woman")
        array.add("girl")
        expected = ["man", "G-string", "girl"]
        actual = array.set(1, "G-string")
        self.assertEqual(expected, actual)


