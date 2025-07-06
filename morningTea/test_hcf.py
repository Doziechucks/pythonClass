from unittest import TestCase
from hcf import return_hcf

class TestHCF(TestCase):
    def test_hcf(self):
        answer = return_hcf(1, 12, 16)
        expected = 1
        self.assertEqual(answer, expected)

    def test_hcf_two(self):
        answer = return_hcf(8, 12, 16)
        expected = 4
        self.assertEqual(answer, expected)

    def test_hcf_three(self):
        answer = return_hcf(8, 12, 16, 2)
        expected = 2
        self.assertEqual(answer, expected)

    def test_hcf_four(self):
        answer = return_hcf(24, 36, 48, 72)
        expected = 12
        self.assertEqual(answer, expected)

    def test_hcf_five(self):
        answer = return_hcf(24, 36, 48, 72, 5)
        expected = 1
        self.assertEqual(answer, expected)

    def test_hcf_six(self):
        answer = return_hcf(4, 6, 10)
        expected = 2
        self.assertEqual(answer, expected)

