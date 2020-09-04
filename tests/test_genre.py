from domainmodel.genre import Genre

def test_init():
    genre1 = Genre("Comedy")
    assert repr(genre1) == "<Genre Comedy>"
    genre2 = Genre("")
    assert genre2.genre_name is None
    genre3 = Genre(42)
    assert genre3.genre_name is None
