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

    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def get_all_users():

    all_users = crud.get_all_users()

    return render_template('all_users.html', all_users = all_users)


@app.route('/users', methods = ["POST"])
def create_account():

    user_email = request.form.get('email')
    user_password = request.form.get('password')

    if crud.get_user_by_email(user_email):
        flash("There is already an account with that email.")
    else:
        crud.create_user(user_email, user_password)
        flash("Your account is created. You can log in")

    return redirect('/')


@app.route('/login', methods = ["POST"])
def login():

    user_email = request.form.get('email')
    user_password = request.form.get('password')

    if crud.get_user_by_email(user_email):
        if crud.get_user_by_email(user_email).password == user_password:
            session['user_email'] = user_email
            flash("Logged in!")
        else:
            flash("Incorrect password, try again.")

    else:
        flash("Email does not exist.")

    return redirect('/')


@app.route('/users/<user_id>')
def show_user_details(user_id):
    
    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
