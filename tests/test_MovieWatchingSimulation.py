from domainmodel.movie import Movie
from domainmodel.user import User
import pytest
from activitysimulations.MovingWatchingSimulation import MovieWatchingSimulation


def test_movie__type_movie():
    movie1 = Movie("Moana", 2016)
    cflix = MovieWatchingSimulation(movie1)
    assert cflix.movie_watched_together == Movie("Moana", 2016)


def test_movie_not_type_movie():
    movie1 = "Moana"
    with pytest.raises(TypeError):
        MovieWatchingSimulation(movie1)


def test_user_not_type_user():
    movie1 = Movie("Moana", 2016)
    cflix = MovieWatchingSimulation(movie1)
    user1 = "Martin"
    review_text1 = "This movie was very enjoyable."
    rating1 = 9
    with pytest.raises(TypeError):
        cflix.create_and_add_review_movie_and_user_to_group_and_individual_list(user1, review_text1, rating1)


def test_review_text_not_string():
    movie1 = Movie("Moana", 2016)
    cflix = MovieWatchingSimulation(movie1)
    user1 = User('Martin', 'pw12345')
    review_text1 = 9
    rating1 = 9
    with pytest.raises(TypeError):
        cflix.create_and_add_review_movie_and_user_to_group_and_individual_list(user1, review_text1, rating1)


def test_rating_not_int():
    movie1 = Movie("Moana", 2016)
    cflix = MovieWatchingSimulation(movie1)
    user1 = User('Martin', 'pw12345')
    review_text1 = "This movie was very enjoyable."
    rating1 = "nine"
    with pytest.raises(TypeError):
        cflix.create_and_add_review_movie_and_user_to_group_and_individual_list(user1, review_text1, rating1)

def test_record_user_and_review_single():
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 107
    user1 = User('Martin', 'pw12345')
    review_text1 = "This movie was very enjoyable."
    rating1 = 9
    cflix = MovieWatchingSimulation(movie1)
    cflix.create_and_add_review_movie_and_user_to_group_and_individual_list(user1, review_text1, rating1)
    assert len(cflix.reviews) == 1
    assert len(cflix.users) == 1



def test_record_user_and_review_multiple():
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 107
    user1 = User('Martin', 'pw12345')
    review_text1 = "This movie was very enjoyable."
    rating1 = 9
    user2 = User('Ashton', 'pw54321')
    review_text2 = "This movie was ok."
    rating2 = 6
    cflix = MovieWatchingSimulation(movie1)
    cflix.create_and_add_review_movie_and_user_to_group_and_individual_list(user1, review_text1, rating1)
    cflix.create_and_add_review_movie_and_user_to_group_and_individual_list(user2, review_text2, rating2)
    assert len(cflix.reviews) == 2
    assert len(cflix.users) == 2


def test_movie_added_to_individual_list():
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 107
    cflix = MovieWatchingSimulation(movie1)
    user1 = User('Martin', 'pw12345')
    review_text1 = "This movie was very enjoyable."
    rating1 = 9
    cflix.create_and_add_review_movie_and_user_to_group_and_individual_list(user1, review_text1, rating1)
    assert user1._watched_movies == [Movie("Moana", 2016)]


def test__review_added_to_individual_list():
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 107
    cflix = MovieWatchingSimulation(movie1)
    user1 = User('Martin', 'pw12345')
    review_text1 = "This movie was very enjoyable."
    rating1 = 9
    cflix.create_and_add_review_movie_and_user_to_group_and_individual_list(user1, review_text1, rating1)
    assert len(user1._reviews) == 1

def test_repr_():
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 107
    user1 = User('Martin', 'pw12345')
    review_text1 = "This movie was very enjoyable."
    rating1 = 9
    user2 = User('Ashton', 'pw54321')
    review_text2 = "This movie was ok."
    rating2 = 6
    cflix = MovieWatchingSimulation(movie1)
    cflix.create_and_add_review_movie_and_user_to_group_and_individual_list(user1, review_text1, rating1)
    cflix.create_and_add_review_movie_and_user_to_group_and_individual_list(user2, review_text2, rating2)
    print(repr(cflix))


