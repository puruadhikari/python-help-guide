"""
You are building a movie recommendation system based on user ratings. Users can rate movies they have seen on a
scale from 1 to 5. Two users are considered to have similar taste in movies if they have both rated the same movie
as 4 or 5.

Your task is to recommend movies to a user based on the following rules:

The user has not rated the movie.
A user with similar taste has rated the movie as 4 or 5.
Write a function that takes a user's name and a collection of ratings, and returns a list of movie recommendations
 for the given user.
"""
from collections import defaultdict


def movie_recommendations(user, ratings) -> list:
    user_dict = defaultdict(list)

    for r in ratings:
        name, movie, rating = r[0], r[1], r[2]
        if int(rating) >= 4:
            user_dict[name].append(movie)

    movie_set = {}

    user_movies = user_dict[user]

    for rated_movie in user_movies:
        for user_1, movies_1 in user_dict.items():
            if user_1 != user and rated_movie in movies_1:
                movie_set[user] = movies_1
    print(movie_set)
    if user in movie_set:
        list1 = movie_set[user]
    else:
        return []
    list2 = user_movies

    result = list(set(list1) - set(list2))
    return result


ratings = [
    ["Alice", "Frozen", "5"],
    ["Bob", "Mad Max", "5"],
    ["Charlie", "Lost In Translation", "4"],
    ["Charlie", "Inception", "4"],
    ["Bob", "All About Eve", "3"],
    ["Bob", "Lost In Translation", "4"],
    ["Dennis", "All About Eve", "5"],
    ["Dennis", "Mad Max", "4"],
    ["Charlie", "Topsy-Turvy", "2"],
    ["Dennis", "Topsy-Turvy", "4"],
    ["Alice", "Lost In Translation", "1"]
]

user = "Bob"

movie_user = defaultdict(list)
user_movie = defaultdict(list)

for name,movie,rating in ratings:
  if int(rating) >= 4:
    movie_user[name].append(movie)
    user_movie[movie].append(name)

movies_by_user = movie_user[user]

rated_users = set()
movies_set = set()
for movie in movies_by_user:
  for usr in user_movie[movie]:
    if usr != user:
      rated_users.add(usr)


for usr_1 in rated_users:
  for movi in movie_user[usr_1]:
    movies_set.add(movi)

print(movies_set-set(movies_by_user))

print(movie_recommendations(user, ratings))
