"""Seed database with set of test data"""

import os
import json
from random import choice, randint 
from datetime import datetime 
import crud, model, server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()


# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    # TODO: get the title, overview, and poster_path from the movie dictionary
    title = movie["title"]
    overview = movie["overview"]
    poster_path = movie["poster_path"]

    # Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    date_str = movie["release_date"]
    date_format = "%Y-%m-%d"
    release_date = datetime.strptime(date_str, date_format)
    
    # TODO: create a movie here and append it to movies_in_db
    new_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(new_movie)


for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # TODO: create a user here
    user = crud.create_user(email, password)

    # TODO: create 10 ratings for the user
    for i in range(10):
        #choose random movie
        movie = choice(movies_in_db)
        #generate random score
        score = randint(1, 5)
        crud.create_rating(user, movie, score)