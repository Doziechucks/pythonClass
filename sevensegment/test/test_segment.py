from segments import Segments
from unittest import TestCase

class TestSegments(TestCase):
    def setUp(self) -> None:
        self.segments = Segments(0,0,0,0,0,0,0,0)
    
    def test_if_upper_is_printed(self):
        actual = self.segments.get_board()
        expected = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        self.assertEqual(actual, expected)
        
