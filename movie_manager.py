"""
Python Practice Exercise: Movie Collection Manager
Objective:
Create a Python program that manages a movie collection using various Python concepts. The program should allow users to:

1. Add movies to the collection.
2. Search for movies by specific criteria.
3. Display all movies in the collection.
4. Handle errors gracefully (e.g., invalid input, missing data).
5. Use object-oriented programming to structure the solution.

Exercise Instructions:

Define a Movie class:
Attributes: title (str), director (str), year (int), rating (float).
Include a method to display a movie's details (__str__ method).

Define a MovieCollection class:
Use a list to store movies.
Methods:
add_movie: Adds a new movie to the collection (accepts args or kwargs).
find_movies: Accepts a keyword argument to filter movies by title, director, or year. Returns matching movies.
display_all_movies: Displays all movies in the collection or a message if the collection is empty.

Error Handling:
Ensure users provide valid input types (e.g., year is an integer, rating is a float).
Handle scenarios where no movies match the search criteria.

Main Functionality:
Implement a main function where users can interact with the movie collection using a menu:

Add a movie.
Search for movies.
Display all movies.
Exit.

Type Hinting:
Use type hints for all function parameters and return types.
"""



class Movie:

    def __init__ (self, title:str, director:str, year:int, rating:float):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating

    def __str__ (self) -> str:

         return f"The title of the movie is '{self.title}' by {self.director} made in {self.year}, the rating is {self.rating}"


class MovieCollection:
    def __init__(self):
        self.movies = []

    def add_movie (self, title:str, director:str, year:int, rating:float):

        movie1 = Movie(title, director, year, rating)

        self.movies.append(movie1)

        print(movie1)

    def display_all_movies (self):
        if not self.movies:
            return None
        else:

            for movie in self.movies:

                print (movie)


    def find_movies (self):
        text = input ("Enter keyword: ")
        for text in self.movies:
            print (text)




def main() -> None:
    collection = MovieCollection()

    while True:
        print("Movie Collection Manager")
        print("1. Add a movie")
        print("2. Search for movies")
        print("3. Display all movies")
        print("4. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                title = input("Title:")
                director = input ("Director:")
                year = input ("Year:")
                rating = input ("Rating:")
                collection.add_movie(title, director, year, rating)
                print("Movie added to the collection")
                # Add a movie
                pass
            elif choice == 2:
                # Search for movies
                collection.find_movies()
                pass
            elif choice == 3:
                # Display all movies
                collection.display_all_movies()
                pass
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                raise ValueError("Invalid choice, please try again.")
        except ValueError:
            print("Error: Please enter a valid choice.")


if __name__ == "__main__":

    main()



