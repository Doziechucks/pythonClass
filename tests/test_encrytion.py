import unittest
from classworkFolder.encryption import encrypt_text


class MyEncryptionCode(unittest.TestCase):
    def test_if_function_exists(self):
        sentence = "Hello, World"
        self.assertTrue(encrypt_text(sentence))

    def test_if_function_printscorrectly(self):
        sentence = "Hello, World"
        expected = "Uryyb, Jbeyq"
        actual = encrypt_text(sentence)
        self.assertEqual(expected, actual)

    def test_if_function_passes_on_integers(self):
        sentence = "Hello 2World5"
        expected = "Uryyb 2Jbeyq5"
        actual = encrypt_text(sentence)
        self.assertEqual(expected, actual)

    def test_if_function_words_on_characters(self):
        sentence = 'a'
        expected = 'n'
        actual = encrypt_text(sentence)
        self.assertEqual(expected, actual)