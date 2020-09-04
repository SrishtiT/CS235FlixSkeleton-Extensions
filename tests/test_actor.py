from domainmodel.actor import Actor


def test_init():
    actor1 = Actor("Angelina Jolie")
    assert repr(actor1) == "<Actor Angelina Jolie>"
    actor2 = Actor("Cameron Diaz")
    assert repr(actor2) == "<Actor Cameron Diaz>"
    actor3 = Actor(42)
    assert actor3.actor_name is None
    actor1.add_actor_colleague(actor2)
    result = actor1.check_if_this_actor_worked_with(actor2)
    assert result is True




