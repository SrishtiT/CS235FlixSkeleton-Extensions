from typing import List
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre


class Movie:

    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self._title = None
        else:
            self._title = title.strip()
        if release_year >= 1990:
            self._release_year = release_year
        else:
            self._release_year = None
        self._description: str = None
        self._director = Director
        self._actors: List[Actor] = list()
        self._genres: List[Genre] = list()
        self._runtime_minutes: int = None

    @property
    def title(self) -> str:
        return self._title

    @property
    def actors(self):
        return self._actors

    @property
    def genres(self):
        return self._genres

    @property
    def description(self):
        return self._description

    @property
    def director(self):
        return self._director

    @property
    def runtime_minutes(self):
        return self._runtime_minutes

    @description.setter
    def description(self, description):
        self._description = description.strip()

    @director.setter
    def director(self, director: Director):
        self._director = director

    @runtime_minutes.setter
    def runtime_minutes(self, minutes):
        if minutes > 0:
            self._runtime_minutes = minutes
        else:
            raise ValueError()

    def add_actor(self, actor: Actor):
        if type(actor) is not Actor:
            return
        self._actors.append(actor)

    def add_genre(self, genre: Genre):
        if type(genre) is not Genre:
            return
        self._genres.append(genre)

    def remove_actor(self, actor: Actor):
        if type(actor) is not Actor:
            return
        if actor in self._actors:
            self._actors.remove(actor)

    def remove_genre(self, genre: Genre):
        if type(genre) is not Genre:
            return
        if genre in self._genres:
            self._genres.remove(genre)

    def __repr__(self):
        return f"<Movie {self._title}, {self._release_year}>"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return (
                other._title == self._title and
                other._release_year == self._release_year
        )

    def __get_unique_string_rep(self):
        return f"{self._title}, {self._release_year}"

    def __lt__(self, other):
        return self.__get_unique_string_rep() < other.__get_unique_string_rep()

    def __hash__(self):
        return hash(self.__get_unique_string_rep())
