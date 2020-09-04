from typing import List
import pytest
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.movie import Movie
from domainmodel.actor import Actor


def test_init():
    movie1 = Movie("Moana", 2016)
    assert repr(movie1) == "<Movie Moana, 2016>"
    movie1.director(Director("Ron Clements"))
    assert "<Director Ron Clements>"
    movie2 = Movie("Kung fu Panda", 1821)
    assert repr(movie2) == "<Movie Kung fu Panda, None>"

def test_runtime_minutes():
    movie1 = Movie("Moana", 2016)
    movie1.runtime_minutes = 120
    assert movie1.runtime_minutes == 120

def test_runtime_minutes_neg():
    movie1 = Movie("Moana", 2016)
    with pytest.raises(ValueError):
        movie1.runtime_minutes = -20

def test_less_than():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Kung fu Panda", 2019)
    assert movie2 < movie1

def test_hash():
    a_set = set()
    movie1 = Movie("Moana", 2016)
    a_set.add(movie1)
    a_set.add(movie1)
    assert len(a_set) == 1

def test_hash_two_movie():
    a_set = set()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Kung fu Panda", 2019)
    a_set.add(movie1)
    a_set.add(movie2)
    assert len(a_set) == 2

def test_actors():
    movie1 = Movie("Moana", 2016)
    actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
    for actor in actors:
        movie1.add_actor(actor)
    assert movie1.actors == actors

def test_description():
    movie1 = Movie("Moana", 2016)
    movie1.description = "fun"
    assert movie1.description == "fun"

def test_genres():
    movie1 = Movie("Moana", 2016)
    genres = [Genre("Comedy"), Genre("Family")]
    for genre in genres:
        movie1.add_genre(genre)
    assert movie1.genres == genres










