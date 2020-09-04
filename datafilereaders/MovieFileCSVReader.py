from typing import List
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.movie import Movie
import csv


class MovieFileCSVReader:
    def __init__(self, file_name: str):
        if file_name == "" or type(file_name) is not str:
            self._file_name = None
        else:
            self._file_name = file_name
        self._dataset_of_movies: List[Movie] = list()
        self._dataset_of_actors = set()
        self._dataset_of_directors = set()
        self._dataset_of_genres = set()

    @property
    def dataset_of_movies(self):
        return self._dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self._dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self._dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self._dataset_of_genres

    def read_csv_file(self):
        input_file = csv.DictReader(open(self._file_name, encoding="utf-8-sig"))
        for row in input_file:
            # movies
            movie = Movie(row["Title"], int(row["Year"]))
            self._dataset_of_movies.append(movie)
            # actors
            each_movie_actors = row["Actors"].split(",")
            for i in range(len(each_movie_actors)):
                actor = Actor(each_movie_actors[i].strip())
                if actor not in self._dataset_of_actors:
                    self._dataset_of_actors.add(actor)
            # directors
            director = Director(row["Director"])
            if director not in self._dataset_of_directors:
                self._dataset_of_directors.add(director)
            # genres
            each_movie_genre = row["Genre"].split(",")
            for i in range(len(each_movie_genre)):
                genre = Genre(each_movie_genre[i].strip())
                if genre not in self._dataset_of_genres:
                    self._dataset_of_genres.add(genre)
