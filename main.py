import movie_storage_sql
import movies as mv

def main():
    print('********** My Movies Database **********')
    condition = True
    while condition:
        movies = movie_storage_sql.list_movies()
        print(movies)
        mv.show_menu()
        try:
            menu_number = int(mv.choice_menu())
            if isinstance(menu_number, int) and 0 <= menu_number <= 10:
                mv.control_menu(menu_number, movies)
                condition = mv.validate_enter()
            else:
                print("Please enter a correct number")
                condition = mv.validate_enter()
        except ValueError:
            print("Please enter a correct number")
            condition = mv.validate_enter()


if __name__ == "__main__":
    main()