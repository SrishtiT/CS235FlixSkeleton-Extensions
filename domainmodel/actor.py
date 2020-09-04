class Actor:
    def __init__(self,  actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self._actor_full_name = None
        else:
            self._actor_full_name = actor_full_name.strip()
        self._colleagues = set()

    @property
    def actor_name(self) -> str:
        return self._actor_full_name

    def __repr__(self):
        return f"<Actor {self._actor_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Actor):
            return False
        return other._actor_full_name == self._actor_full_name

    def __lt__(self, other):
        return self._actor_full_name < other._actor_full_name

    def __hash__(self):
        return hash(self._actor_full_name)

    def add_actor_colleague(self, colleague):
        self._colleagues.add(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self._colleagues:
            return True
        return False



