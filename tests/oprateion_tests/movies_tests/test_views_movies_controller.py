import pytest
from pydantic import ValidationError
from rest_framework.test import APIRequestFactory

from apiapp.operations.movies import MoviesController
from apiapp.services.movies import Movie as MovieDomainModel
from apiapp.services.movies import MovieService


@pytest.fixture(scope="function")
def factory():
    return APIRequestFactory()


class TestMoviesControllerPostShould:
    """Tests for Movies Controller post which creates multiple movies"""

    def test_pass_with_correct_payload(self, factory, mocker):
        return_value = [MovieDomainModel(id=1, title="test movie")]
        mocker.patch(
            "apiapp.services.movies.MovieService.create_movies",
            return_value=return_value,
        )
        request = factory.post(
            "/movies/",
            {"movies": [{"title": "movie34", "description": "desc2"}]},
            format="json",
        )
        view = MoviesController.as_view()
        response = view(request)

        assert response.status_code == 200
        assert (
            response.content
            == b'{"movies": [{"id": "1", "title": "test movie", "description": null, "release_date": null}]}'
        )

    def test_fail_when_title_is_null(self, factory, mocker):
        mocker.patch("apiapp.services.movies.MovieService.create_movies")
        request = factory.post("/movies/", format="json")
        view = MoviesController.as_view()
        with pytest.raises(ValidationError) as exc_info:
            view(request)
        assert exc_info.value.errors() == [
            {
                "loc": ("__root__", "movies"),
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
        MovieService.create_movies.assert_not_called()


class TestMoviesControllerGetShould:
    """Tests for Movies Controller get  which returns multiple movies"""

    def test_return_list_of_movies(self, factory, mocker):
        return_value = [MovieDomainModel(id=1, title="test")]
        mocker.patch(
            "apiapp.services.movies.MovieService.get_movies", return_value=return_value
        )
        request = factory.get("/movies?title=test", format="json")
        view = MoviesController.as_view()
        response = view(request)

        assert response.status_code == 200
        assert (
            response.content
            == b'{"movies": [{"id": "1", "title": "test", "description": null, "release_date": null}]}'
        )
