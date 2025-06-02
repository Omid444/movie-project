import statistics
from statistics import median
import random
#import matplotlib.pyplot as plt
import movie_storage_sql
import sys

def show_menu():
    """Print all menu."""
    menu = '''Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Create Rating Histogram'''
    print(menu)


def choice_menu()->int:
    """Get user data, return data integer."""
    menu_num =input('\nEnter Choice (0-9): ')
    return menu_num
    print("Please enter the corret number")


def exit_program(movies_list):
    """Print 'Bye' for user and exit program."""
    print('Bye')
    sys.exit()


def show_movie_list(movies_list):
    """Print all movies info."""
    for movie, rate_year in movies_list.items():
        print(f'{movie}, {rate_year["rating"]}, {rate_year["year"]}')


def add_movie(movies_list):
    """Get info from user, add data to the list, print confirmation."""
    while True:
        movie_name = (input('Enter movie name: ')).lower()
        if movie_name.title() not in movies_list:
            movie_rate = float(input('Enter movie rating: '))
            if  1 < movie_rate < 10:
                movie_year = int(input("Enter movie's year: "))
                movie_country = input("Enter movie's country:")
                movie_storage_sql.add_movie(movie_name.title(), movie_year, movie_rate, movie_country)
                print(f'your movie {movie_name} added successfully')
                return
        else:
            print(f"Movie {movie_name} already exist!")

def delete_movie(movies_list):
    """Get data from user, delete movie, print confirmation."""
    movie_name = (input('Enter movie name: ')).lower()
    for movie in movies_list:
        if movie_name.title() == movie:
            movie_storage_sql.delete_movie(movie_name.title())
            print(f'your movie {movie_name.title()} deleted successfully')
            return
    print(f'The movie {movie_name.title()} does not exist')


def update_movie(movies_list):
    """Get rating data from user, update movie's rating, print confirmation."""
    movie_name = (input('Enter movie name: ')).lower()
    for movie in movies_list:
        if movie_name.title() == movie:
            movie_rate = float(input('Enter new movie rating: '))
            movie_storage_sql.update_movie(movie_name.title(), movie_rate)
            print('New rating successfully updated')
            return
    print(f'The movie {movie_name.title()} does not exist')


def find_best_movies(movies)->dict:
    """Find the best movie or movies from another dictionary key=movie and value=rating."""
    best_movie= max(movies.values())
    best_movies = {key:value for key,value in movies.items() if value  == best_movie}
    return best_movies


def find_worst_movie(movies)->dict:
    """Find the worst movie or movies from another dictionary key=movie and value=rating."""
    worst_movie = min(movies.values())
    worst_movies = {key: value for key, value in movies.items() if value == worst_movie}
    return worst_movies


def calculate_average_rating(movies):
    """From another dictionary calculate average rating."""
    return statistics.mean(movies.values())


def  calculate_median_rate(movies)->float:
    """From another dictionary calculate median rating."""
    return median(list(movies.values()))


def make_movie_dict(movies_list):
    """Make a new dictionary to support other function (key=movie and value=rating)."""
    movies_rating_dict = {}
    for movie in movies_list:
        movies_rating_dict[movie] = movies_list[movie]["rating"]
    return movies_rating_dict


def show_stats(movies_list):
    """print stats info."""
    movies_rating_dict = make_movie_dict(movies_list)

    best_movies = find_best_movies(movies_rating_dict)

    worst_movies = find_worst_movie(movies_rating_dict)

    average_rating = calculate_average_rating(movies_rating_dict)

    median_rate = calculate_median_rate(movies_rating_dict)

    print(f'Average rating: {average_rating:.2f}\n')
    print(f'Median rating: {median_rate:.2f}\n')
    for movie, rating in best_movies.items():
        print(f'The best movie: {movie}:{rating}')
    print()
    for movie, rating in worst_movies.items():
        print(f'The worst movie: {movie}: {rating}')


def show_random_movie(movies_list):
    """Print a random movie info."""
    random_movie = random.choice(list(movies_list.keys()))
    print(f'{random_movie}, {movies_list[random_movie]["rating"]}, {movies_list[random_movie]["year"]}')


def search_movie(movies_list):
    """Get movie title from user, print movie."""
    user_input = input('Enter movie name: ').lower()
    for movie in movies_list:
        if user_input.title() in movie:
            print(f'{movie.title()}, {movies_list[movie]["rating"]}, {movies_list[movie]["year"]} ')

def get_value(movie):
    """This is only for sorted function key."""
    return movie[1]["rating"]

def sort_movie_by_rating(movies_list):
    """Make new sorted list, print info."""
    sorted_dict = dict(sorted(movies_list.items(), key=get_value , reverse= True))
    print(sorted_dict)
    for movie, info in sorted_dict.items():
        print(f'{movie.title()}, {info["rating"]}, {info["year"]} ')


def show_histogram(movies_list):
    """Show movie's rating histogram."""
    movies_rating_dict = make_movie_dict(movies_list)
    rating_list = list(movies_rating_dict.values())
    plt.hist(rating_list)
    plt.show()

def validate_enter():
    """Validate if enter key is pressed"""
    while True:
        user_input = input('\nPress Enter to continue ')
        if user_input == '' or user_input.isspace():
            return True
        else:
            print("")

def control_menu(number_selected, list_of_movies):
    """Select function base on th menu that user has selected."""
    menu_dict = {0:exit_program,1:show_movie_list,2:add_movie, 3:delete_movie, 4:update_movie,
                 5:show_stats, 6:show_random_movie, 7:search_movie, 8:sort_movie_by_rating,
                 9:show_histogram}
    for menu_number, menu in menu_dict.items():
        if menu_number == number_selected:
            menu(list_of_movies)

def main():
    print('********** My Movies Database **********')
    condition = True
    while condition:
        movies = movie_storage_sql.list_movies()
        show_menu()
        try:
            menu_number = int(choice_menu())
            if isinstance(menu_number, int) and 0 <= menu_number <10:
                control_menu(menu_number, movies)
                condition = validate_enter()
            else:
                print("Please enter a correct number")
                condition = validate_enter()
        except ValueError:
            print("Please enter a correct number")
            condition = validate_enter()


if __name__ == "__main__":
    main()
