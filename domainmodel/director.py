class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self._director_full_name = None
        else:
            self._director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self._director_full_name

    def __repr__(self):
        return f"<Director {self._director_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Director):
            return False
        return other._director_full_name == self._director_full_name

    def __lt__(self, other):
        return self._director_full_name < other._director_full_name


    def __hash__(self):
        return hash(self._director_full_name)

