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



# You are given a list called "users".

# Implement the following two functions:

# 1. function "filter_all_or_nothing_people" - takes the "users" list as an argument and
# for the given list returns a list of users who either have no pets at all or have both a dog and a cat.


# 2. function "filter_underaged_owners" - takes the "users" list as an argument and
# for the given list returns a list of users who are not yet of legal age but already have at least one pet.

users = [
    {'id': '1', 'name': 'John Smith', 'age': 17, 'hasDog': True, 'hasCat': True}, #filter
    {'id': '2', 'name': 'Ann Smith', 'age': 24, 'hasDog': True, 'hasCat': False},
    {'id': '3', 'name': 'Tom Jones', 'age': 63, 'hasDog': True, 'hasCat': True}, #filter
    {'id': '4', 'name': 'Rose Peterson', 'age': 20, 'hasDog': True, 'hasCat': False},
    {'id': '5', 'name': 'Alex John', 'age': 25, 'hasDog': False, 'hasCat': False}, #filter
    {'id': '6', 'name': 'Ronald Jones', 'age': 31, 'hasDog': False, 'hasCat': True},
    {'id': '7', 'name': 'Elton Smith', 'age': 16, 'hasDog': True, 'hasCat': False},
    {'id': '8', 'name': 'Simon Peterson', 'age': 32, 'hasDog': False, 'hasCat': True},
    {'id': '9', 'name': 'Daniel Cane', 'age': 15, 'hasDog': False, 'hasCat': False}, #filter
]

def filter_all_or_nothing_people (list_users:list) -> list:
    list_pet_status = []
    names = []
    for user in list_users:
        if (user["hasDog"] == True and user["hasCat"] == True) or (user["hasDog"] == False and user["hasCat"] == False):
            list_pet_status.append(user)
    for user2 in list_pet_status:
         names.append(user2["name"])

    return  print("neturi arba turi abu gyvunus:", names)

def filter_underaged_owners (list_users) -> list:
    list_legal_age =[]
    names = []
    for user in list_users:
        if user["age"] < 18 and (user["hasDog"] == True or user["hasCat"] == True):
            list_legal_age.append(user)
    for user3 in list_legal_age:
         names.append(user3["name"])

    return  print("nera legalaus amziaus:", names)
    return list_legal_age





filter_all_or_nothing_people (users)
filter_underaged_owners (users)


# Create a Dog class with the following attributes and methods:

# Attributes:
# - name (string)
# - breed (string)
# - age (integer)

# Methods:
# - is_old() - if the dog is older than 12 years then returns True, otherwise - False.

# Create two instances of the Dog class, make one young and one old, call the is_old
# method on both of them and print the results

class Dog:

    def __init__(self, name:str, breed:str, age:int):
        self.name = name
        self.breed = breed
        self.age = age


    def is_old(self) -> bool:

        if self.age > 12:
            return True
        else:
            return False


dog1 = Dog (name = "Kudlius", breed = "Kolis", age = 13)
dog2 = Dog (name = "Pupa", breed = "Taksas", age = 7)


print(dog1.name, "is old?", dog1.is_old())
print(dog2.name, "is old?", dog2.is_old())
