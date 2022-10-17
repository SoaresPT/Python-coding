def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    database.append({"name": name, "director": director, "year": year, "runtime": runtime})
    return database


def search_movies(database: list, search_word: str):
    new_list = []
    for i in range(len(database)):
        if search_word in database[i]["name"]:
            new_list.append(database[i])
    return new_list


movies = []
add_movie(movies, "Beetlejuice", "Tim Burton", 1988, 92)
add_movie(movies, "The Cotton Club", "Francis Ford Coppola", 1984, 127)
add_movie(movies, "The Shawshank Redemption", "Frank Darabont", 1994, 142)
add_movie(movies, "Crocodile Dundee", "Peter Faiman", 1986, 97)
add_movie(movies, "Valkyrie", "Bryan Singer", 2008, 121)
add_movie(movies, "Memento", "Christopher Nolan", 2000, 113)
add_movie(movies, "The Lord of the Rings The Return of the King", "Peter Jackson", 2003, 201)
add_movie(movies, "The Lord of the Rings The Fellowship of the Ring", "Peter Jackson", 2001, 178)
add_movie(movies, "The Lord of the Rings", "Peter Jackson", 2001, 178)
print(f"Complete movie list:")
print(f"{movies}")
print("\n")
print(search_movies(movies, "Crocodile"))
print(search_movies(movies, "The Shawshank Redemption"))
print(search_movies(movies, "The Lord of the Rings"))
