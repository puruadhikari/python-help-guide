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

user = "Bob"
def movie_recommendations_new(user,ratings):
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

    return list(movies_set-set(movies_by_user))


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

print(movie_recommendations_new(user, ratings))
