from domainmodel.movie import Movie
from domainmodel.review import Review


def test_normal_review():
    movie = Movie("Moana", 2016)
    review_text = "This movie was very enjoyable."
    rating = 10
    review = Review(movie, review_text, rating)
    assert repr(review.movie) == "<Movie Moana, 2016>"
    assert review.review_text == "This movie was very enjoyable."
    assert review.rating == 10

def test_negative_rating():
    movie = Movie("Moana", 2016)
    review_text = "This movie was very enjoyable."
    rating = -10
    review = Review(movie, review_text, rating)
    assert review.rating == None

def test_extreme_rating():
    movie = Movie("Moana", 2016)
    review_text = "This movie was very enjoyable."
    rating = 100
    review = Review(movie, review_text, rating)
    assert review.rating == None

def test_string_rating():
    movie = Movie("Moana", 2016)
    review_text = "This movie was very enjoyable."
    rating = "a"
    review = Review(movie, review_text, rating)
    assert review.rating == None

def test_int_review():
    movie = Movie("Moana", 2016)
    review_text = 5
    rating = 10
    review = Review(movie, review_text, rating)
    assert review.review_text == None



