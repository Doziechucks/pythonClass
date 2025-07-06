from src.movieapp.movie import Movie
from datetime import datetime

class Movies:
    def __init__(self):
        self.__movie_list: [Movie] = []
        self.__movie_dict = {}
        self.__all_movie_dict = {}
        self.__movie_rating_list = []


    def create_movie_list(self, movie):
        movie_title = movie.lower()
        for movie in self.__movie_list:
            if movie_title == movie.get_title:
                return "movie added"
        else:
            movie_information = Movie(movie_title)
            self.__movie_list.append(movie_information)
            self.create_movie_dict()

    def create_movie_dict(self):
        for movie in self.__movie_list:
            self.__all_movie_dict[movie.get_title] = []

    def get_movie_dict(self):
        for movie in self.__movie_list:
            self.__movie_dict[movie.title] = []

    def get_list_of_movies(self):
        movie_titles = ""
        for movie in self.__all_movie_dict.keys():
            movie_titles = movie_titles + movie + "\n"
        return movie_titles

    def rate_movie(self, movie_title, rating):
        for movie in self.__all_movie_dict.keys():
            if movie == movie_title:
                self.__all_movie_dict[movie].append(rating)
                self.__movie_rating_list.append(rating)

    def get_average_rating_of_a_movie(self, movie_title):
        for movie in self.__all_movie_dict.keys():
            if movie == movie_title:
                return sum(self.__all_movie_dict[movie]) / len(self.__all_movie_dict[movie])

    def get_average_rating_of_all_movies(self):
        return f"{sum(self.__movie_rating_list) / len(self.__movie_rating_list)}: is average rating for all movies"

    def movie_checker(self, movie_title):
        for movie in self.__all_movie_dict.keys():
            if movie == movie_title:
                return True
        else: return False

    def get_all_movies_length_dict(self):
        return len(self.__all_movie_dict)

    def get_movie_list_length(self):
        return len(self.__movie_list)

    def get_length_of_rating_list(self):
        return len(self.__movie_rating_list)




