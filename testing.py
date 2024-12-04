
movies = []

while True:
    movie = input("Movie:")
    movies.append(movie)
    continue_or_not = input("say yes if continue:")
    if not continue_or_not == "yes":
        break
for movie in movies:
    print(movie)