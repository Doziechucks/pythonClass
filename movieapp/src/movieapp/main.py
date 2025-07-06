from src.movieapp.movies import Movies

movies = Movies()

def main():
    menu = input("""
    1. Add a movie
    2. Rate a movie
    3. get average for a movie
    4. get average ratings for all movies
    5. press any other key to quit
    : """)

    match menu:
        case "1":
            add_movie()
        case "2":
            rate_a_movie()
        case "3":
            get_average_rating_for_a_movie()
        case "4":
            get_average_rating_for_all_movies()
        case "5":
            quit()
        case _:
            print("Invalid input")
            main()

def add_movie():
    number = movies.get_movie_list_length()
    movie = input("Enter movie title: ")
    movie_name = movie.strip()
    if movie_name == "":
        print("Please enter a valid movie title.")
    else:
        movies.create_movie_list(movie_name)
        movies.create_movie_dict()
        checking = movies.get_movie_list_length()
        if checking == number + 1:
            print("movie added successfully")
        else:
            print("movie already exists")
    main()

def check_movie(movie_name):
    if movies.movie_checker(movie_name):
        return True
    else:
        return False



def rate_a_movie():
    check = movies.get_list_of_movies()
    if check == "":
        print("No movies found.")
    else:
        print(f"the movies available are\n" + check)

        checker = False
        movie_name = input("Enter movie title: ")
        if check_movie(movie_name):
            checker = True
        while not checker:
            movie_name = input("Enter movie in the movie list: ")
            if check_movie(movie_name):
                checker = True
            else:
                checker = False

        validate = False
        movie_rating = input("Enter movie rating: ")
        if movie_rating.isdigit() and 0 < int(movie_rating) <= 5:
            the_movie_rating = int(movie_rating)
            movies.rate_movie(movie_name, the_movie_rating)
            validate = True
        while not validate:
            movie_rating = input("Enter a correct movie rating between 0 and 5: ")
            if movie_rating.isdigit() and 0 < int(movie_rating) <= 5:
                the_movie_rating = int(movie_rating)
                movies.rate_movie(movie_name, the_movie_rating)
                validate = True
                print("rating successful")
            else:
                validate = False

    main()

def get_average_rating_for_a_movie():
    check = movies.get_list_of_movies()
    if check == "":
        print("No movies found.")
    else:
        print(f"the movies available are\n" + check)

        checker = False
        movie_name = input("Enter movie title: ")
        if check_movie(movie_name):
            checker = True
        while not checker:
            movie_name = input("Enter a movie title in the movie list: ")
            if check_movie(movie_name):
                checker = True
            else:
                checker = False


        average_rating = movies.get_average_rating_of_a_movie(movie_name)
        print(average_rating)
    main()

def get_average_rating_for_all_movies():
    check = movies.get_list_of_movies()
    if check == "":
        print("No movies found.")
    else:
        movie_ratings = movies.get_average_rating_of_all_movies()
        print(movie_ratings)
    main()

main()
