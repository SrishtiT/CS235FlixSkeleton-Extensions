from datafilereaders.MovieFileCSVReader import MovieFileCSVReader


def test_dataset_lengths():
    movie_file_reader = MovieFileCSVReader("../datafiles/Data1000Movies.csv")
    movie_file_reader.read_csv_file()
    length_movies = len(movie_file_reader._dataset_of_movies)
    length_actors = len(movie_file_reader._dataset_of_actors)
    length_directors = len(movie_file_reader._dataset_of_directors)
    length_genres = len(movie_file_reader._dataset_of_genres)
    assert length_movies == 1000
    assert length_actors == 1985
    assert length_directors == 644
    assert length_genres == 20



