"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_home():

    return render_template('homepage.html')

@app.route('/movies')
def get_all_movies():

    all_movies = crud.get_all_movies()

    return render_template('all_movies.html', all_movies = all_movies)


@app.route('/movies/<movie_id>')
def show_movie_details(movie_id):
    
    movie = crud.get_movie_by_id(movie_id)
    print("*"*20)
    print(movie)
    print("*"*20)

    return render_template('movie_details.html', movie=movie)


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
