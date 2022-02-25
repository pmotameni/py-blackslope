from pydantic import ValidationError
from apiapp.operations.movies import MovieController
from apiapp.services.movies import Movie as MovieDomainModel, MovieService
import pytest
from rest_framework.test import APIRequestFactory


@pytest.fixture(scope="function")
def factory():
    return APIRequestFactory()


class TestMovieControllerGetShould:
    '''Tests for Movies Controller get  which returns multiple movies'''

    def test_return_single_movie(self, factory, mocker):
        return_value = MovieDomainModel(id=1, title="test movie")
        mocker.patch("apiapp.services.movies.MovieService.get_movie",
                     return_value=return_value)
        request = factory.get("/movies/", format='json')
        view = MovieController.as_view()
        response = view(request, id=1)

        MovieService.get_movie.assert_called_once_with(1)
        assert response.status_code == 200
        assert response.content == b'{"movie": {"id": "1", "title": "test movie", "description": null, "release_d' b'ate": null}}'
