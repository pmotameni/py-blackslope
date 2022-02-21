from apiapp.operations.movies import MoviesController
from apiapp.services.movies import Movie as MovieDomainModel
import pytest
from rest_framework.test import APIRequestFactory


@pytest.fixture(scope="function")
def factory():
    return APIRequestFactory()


def test_single(factory, mocker):
    return_value = [MovieDomainModel(id=1, title="test movie")]
    mocker.patch("apiapp.services.movies.MovieService.get_movies",
                 return_value=return_value)
    request = factory.get("/movies/", format='json')
    view = MoviesController.as_view()
    response = view(request)
    assert response.status_code == 200
    assert response.content == b'{"movies": [{"id": "1", "title": "test movie", "description": null, "release_date": null}]}'
