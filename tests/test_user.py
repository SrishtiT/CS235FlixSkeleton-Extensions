from domainmodel.movie import Movie
from domainmodel.user import User


def test_normal_user():
    user1 = User('Martin', 'pw12345')
    assert repr(user1) == "<User martin>"
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 107
    user1.watch_movie(movie1)
    assert user1._watched_movies == [Movie("Moana", 2016)]
    assert user1.time_spent_watching_movies_minutes == 107

