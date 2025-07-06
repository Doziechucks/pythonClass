from datetime import datetime

from src.movieapp.movie import Movie
from unittest import TestCase


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("movie name1")

    def test_that_that_movie_can_get_title(self):
        self.assertEqual(self.movie.get_title, "movie name1")

    def test_that_movie_time_is_updated(self):
        self.assertEqual(self.movie.get_upload_time(), datetime.now().replace(microsecond=0))

