from domainmodel.watchlist import WatchList
from domainmodel.movie import Movie
import pytest


def test_check_size():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Mulan", 2020)
    watchlist1 = WatchList()
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    assert watchlist1.size() == 2


def test_check__size_empty():
    watchlist1 = WatchList()
    assert watchlist1.size() == 0


def test_add_movie_not_type_movie():
    movie1 = "Moana"
    watchlist1 = WatchList()
    with pytest.raises(TypeError):
        assert watchlist1.add_movie(movie1)


def test_add_same_movie_again():
    movie1 = Movie("Moana", 2016)
    watchlist1 = WatchList()
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie1)
    assert watchlist1.size() == 1


def test_remove_movie_which_is_not_in_watchlist():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Mulan", 2020)
    watchlist1 = WatchList()
    watchlist1.add_movie(movie1)
    watchlist1.remove_movie(movie2)
    assert watchlist1.size() == 1


def test_remove_movie():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Mulan", 2020)
    watchlist1 = WatchList()
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    watchlist1.remove_movie(movie2)
    assert watchlist1.size() == 1

def test_remove_movie_not_type_movie():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Mulan", 2020)
    watchlist1 = WatchList()
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    watchlist1 = WatchList()
    with pytest.raises(TypeError):
        assert watchlist1.add_movie("Moana")


def test_select_movie_to_watch_index_ok():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Mulan", 2020)
    watchlist1 = WatchList()
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    assert watchlist1.select_movie_to_watch(1) == Movie("Mulan", 2020)


def test_select_movie_to_watch_index_not_int():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Mulan", 2020)
    watchlist1 = WatchList()
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    with pytest.raises(TypeError):
        assert watchlist1.select_movie_to_watch("a")


def test_select_movie_to_watch_index_out_of_bounds_positive():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Mulan", 2020)
    watchlist1 = WatchList()
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    assert watchlist1.select_movie_to_watch(2) == None


def test_select_movie_to_watch_index_out_of_bounds_negative():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Mulan", 2020)
    watchlist1 = WatchList()
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    assert watchlist1.select_movie_to_watch(-1) == None


def test_first_movie_in_watchlist():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Mulan", 2020)
    watchlist1 = WatchList()
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    assert watchlist1.first_movie_in_watchlist() == Movie("Moana", 2016)


def test_first_movie_in_watchlist_empty():
    watchlist1 = WatchList()
    assert watchlist1.first_movie_in_watchlist() == None

def test_help_select_movie_to_watch_nonempty():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Mulan", 2020)
    movie3 = Movie("Frozen", 2014)
    movie4 = Movie("Despicable Me", 2013)
    watchlist1 = WatchList()
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    watchlist1.add_movie(movie3)
    watchlist1.add_movie(movie4)
    assert watchlist1.help_select_movie_to_watch() in [Movie("Moana", 2016), Movie("Mulan", 2020), Movie("Frozen", 2014), Movie("Despicable Me", 2013)]


def test_help_select_movie_to_watch_empty():
    watchlist1 = WatchList()
    assert watchlist1.help_select_movie_to_watch() == None


def test_iterator():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Mulan", 2020)
    movie3 = Movie("Frozen", 2014)
    movie4 = Movie("Despicable Me", 2013)
    watchlist1 = WatchList()
    watchlist1.add_movie(movie1)
    watchlist1.add_movie(movie2)
    watchlist1.add_movie(movie3)
    watchlist1.add_movie(movie4)
    for index, movie in enumerate(watchlist1):
        assert repr(movie) == repr(watchlist1.select_movie_to_watch(index))








