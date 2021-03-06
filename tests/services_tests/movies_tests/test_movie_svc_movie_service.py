import pytest

from apiapp.repositories.movies import Movie as MovieDTO
from apiapp.repositories.movies import MovieRepository
from apiapp.services.movies import Movie as MovieDomainModel
from apiapp.services.movies import MovieService


@pytest.fixture(scope="function")
def service():
    return MovieService(MovieRepository())


class TestMovieServiceCreateMoviesShould:
    def test_call_repo_with_correct_type(self, service, mocker):
        src_dm = [MovieDomainModel(title="test movie")]
        src_dto = [MovieDTO(title="test movie")]

        mocker.patch("apiapp.repositories.movies.MovieRepository.create_movies")

        service.create_movies(src_dm)

        assert (
            MovieRepository.create_movies.call_args_list[0][0][0][0].title
            == src_dto[0].title
        )
        MovieRepository.create_movies.assert_called_once()


class TestMovieServiceDeleteMoviesShould:
    def test_call_repository_with_correct_id(self, service, mocker):
        mocker.patch("apiapp.repositories.movies.MovieRepository.delete_movie")
        service.delete_movie("1001")

        MovieRepository.delete_movie.assert_called_once_with("1001")


class TestMovieServiceGetMovieShould:
    def test_call_repository_with_correct_id(self, service, mocker):
        return_dto = MovieDTO(id="1001", title="test movie")
        mocker.patch(
            "apiapp.repositories.movies.MovieRepository.get_movie",
            return_value=return_dto,
        )
        service.get_movie("1001")

        MovieRepository.get_movie.assert_called_once_with("1001")


class TestMovieServiceGetMoviesShould:
    def test_call_repository_with_correct_id(self, service, mocker):
        return_dto = [MovieDTO(id="1", title="test movie")]
        mocker.patch(
            "apiapp.repositories.movies.MovieRepository.get_movies",
            return_value=return_dto,
        )
        service.get_movies()

        MovieRepository.get_movies.assert_called_once()

    def test_return_movies_with_search_term(self, service, mocker):
        search_term = "my title"
        result_dms = [MovieDomainModel(id="1001", title="test movie")]
        src_dto = [MovieDTO(id="1001", title="test movie")]
        mocker.patch(
            "apiapp.repositories.movies.MovieRepository.search_movies",
            return_value=src_dto,
        )

        results = service.get_movies(search_term)

        MovieRepository.search_movies.assert_called_once_with(search_term)
        assert results == result_dms


class TestMovieServiceUpdateMovieShould:
    def test_call_repository_with_correct_id(self, service, mocker):
        src_dm = MovieDomainModel(id="1001", title="test movie")
        src_dto = MovieDTO(id="1001", title="test movie")
        mocker.patch("apiapp.repositories.movies.MovieRepository.update_movie")

        service.update_movie(src_dm)

        MovieRepository.update_movie.assert_called_once_with(src_dto)
