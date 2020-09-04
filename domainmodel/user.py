from domainmodel.movie import Movie
from domainmodel.review import Review
from typing import List


class User:
    def __init__(self, user_name: str, password: str):
        if user_name == "" or type(user_name) is not str:
            self._user_name = None
        else:
            self._user_name = user_name.strip().lower()
        self._password = password
        self._watched_movies: List[Movie] = list()
        self._reviews: List[Review] = list()
        self._time_spent_watching_movies_minutes: int = 0

    @property
    def user_name(self):
        return self._user_name

    @property
    def password(self):
        return self._password

    @property
    def watched_movies(self):
        return self._watched_movies

    @property
    def reviews(self):
        return self._reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self._time_spent_watching_movies_minutes

    def watch_movie(self, movie: Movie):
        self._watched_movies.append(movie)
        self._time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review: Review):
        self._reviews.append(review)

    def __repr__(self):
        return f"<User {self._user_name}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return (
                other._user_name == self._user_name
        )

    def __lt__(self, other):
        return self._user_name < other._user_name

    def __hash__(self):
        return hash(self._user_name)
