from apiapp.operations.movies import MovieController
from apiapp.services.movies import Movie as MovieDomainModel, MovieService
import pytest
from rest_framework.test import APIRequestFactory


@pytest.fixture(scope="function")
def factory():
    return APIRequestFactory()


class TestMovieControllerGetShould:
    '''Tests for Movie Controller get  which return single movie'''

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


class TestMovieControllerPutShould:
    def test_update_single_movie(self, factory, mocker):
        '''Tests for Movie Controller put which update a single movie'''

        mocker.patch("apiapp.services.movies.MovieService.update_movie")
        request = factory.put("/movies/1/",
                              {
                                  "movie": {
                                      "id": "1",
                                      "title": "test movie",
                                      "description": "desc2"
                                  }
                              }, format='json')
        view = MovieController.as_view()
        response = view(request, id=1)
        movie_dm = MovieDomainModel(id=1, title="test movie",
                                    description="desc2")

        MovieService.update_movie.assert_called_once_with(movie_dm)
        assert response.status_code == 204


class TestMovieControllerDeleteShould:
    def test_delete_single_movie(self, factory, mocker):
        '''Tests for Movie Controller put which update a single movie'''

        mocker.patch("apiapp.services.movies.MovieService.delete_movie")
        request = factory.delete("/movies/1/")
        view = MovieController.as_view()
        response = view(request, id=1)

        MovieService.delete_movie.assert_called_once_with(1)
        assert response.status_code == 204
