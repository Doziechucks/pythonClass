from src.movieapp.movies import Movies
from unittest import TestCase

class TestMovie(TestCase):
    def setUp(self):
        self.movies = Movies()

    def test_that_create_movie_adds_to_movie_list(self):
        self.movies.create_movie_list("man")
        self.movies.create_movie_list("woman")
        self.assertEqual(2, self.movies.get_movie_list_length())

    def test_if_movie_is_added(self):
        self.movies.create_movie_list("movie name1")
        self.movies.create_movie_list("movie name2")
        self.movies.create_movie_dict()
        self.assertEqual(2, self.movies.get_all_movies_length_dict())

    def test_if_movie_movie_can_be_rated(self):
        self.movies.create_movie_list("movie name1")
        self.movies.create_movie_dict()
        self.movies.rate_movie("movie name1", 3)
        expected = 3
        actual = self.movies.get_average_rating_of_a_movie("movie name1")
        self.assertEqual(expected, actual)

    def test_that_movie_can_be_rated_multiple_times(self):
        self.movies.create_movie_list("movie name1")
        self.movies.create_movie_dict()
        self.movies.rate_movie("movie name1", 3)
        self.movies.rate_movie("movie name1", 5)
        expected = 4
        actual = self.movies.get_average_rating_of_a_movie("movie name1")
        self.assertEqual(expected, actual)

    def test_if_average_of_all_is_seen(self):
        self.movies.create_movie_list("movie name1")
        self.movies.create_movie_list("movie name2")
        self.movies.create_movie_dict()
        self.movies.rate_movie("movie name1", 3)
        self.movies.rate_movie("movie name1", 5)
        self.movies.rate_movie("movie name2", 3)
        self.movies.rate_movie("movie name2", 5)
        expected = "4.0: is average rating for all movies"
        self.assertEqual(expected, self.movies.get_average_rating_of_all_movies())

    def test_that_movie_is_not_rated_when_rated_above_5(self):
        self.movies.create_movie_list("movie name2")
        self.movies.create_movie_dict()
        self.movies.rate_movie("movie name1", 7)
        self.assertEqual(0, self.movies.get_length_of_rating_list())

    def test_that_same_movie_cannot_be_added_twice(self):
        self.movies.create_movie_list("movie name1")
        self.movies.create_movie_list("movie name1")
        self.assertEqual(1, self.movies.get_movie_list_length())

    def test_that_lower_and_upper_case_is_seen_as_the_same(self):
        self.movies.create_movie_list("movie name1")
        self.movies.create_movie_list("movie NAme1")
        self.assertEqual(1, self.movies.get_movie_list_length())
















