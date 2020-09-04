from datetime import datetime
from domainmodel.movie import Movie

class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        self._movie: Movie = movie
        if review_text == "" or type(review_text) is not str:
            self._review_text = None
        else:
            self._review_text = review_text
        if type(rating) is not int:
            self._rating = None
        elif rating > 10 or rating < 1:
            self._rating = None
        else:
            self._rating = rating
        self._timestamp = datetime.today()

    @property
    def movie(self):
        return self._movie

    @property
    def review_text(self):
        return self._review_text

    @property
    def rating(self):
        return self._rating

    @property
    def timestamp(self):
        return self._timestamp

    def __repr__(self):
        return f"<Movie {self._movie}> \nReview: {self._review_text} \nRating:" \
               f" {self._rating} \nTimestamp: {self._timestamp}"

    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        return (
                other._movie == self._movie and
                other._review_text == self._review_text and
                other._rating == self._rating and
                other._timestamp == self._timestamp
        )




