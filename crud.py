"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_all_users():

    return User.query.all()


def get_user_by_id(user_id):

    return User.query.get(user_id)


def get_user_by_email(user_email):

    return User.query.filter_by(email=user_email).first()


def create_rating(user, movie, score):
    """Create a rating with User instance and Movie instance"""

    movie_rating = Rating(user=user, movie=movie, score=score)

    db.session.add(movie_rating)
    db.session.commit()


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie


def get_all_movies():

    return Movie.query.all()


def get_movie_by_id(movie_id):

    # return Movie.query.filter_by(movie_id=movie_id)
    return Movie.query.get(movie_id)



if __name__ == '__main__':
    from server import app
    connect_to_db(app)