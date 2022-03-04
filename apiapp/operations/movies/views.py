from automapper import mapper
from django.http import JsonResponse
from pydantic import parse_obj_as
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView as APIController

from apiapp.services.movies import Movie as MovieDomainModel
from apiapp.services.movies import MovieService

# Create your controllers and endpoints here.
from ...common.decorators.strong_type import strong_type
from .viewmodels import (
    CreateMovie,
    CreateMoviesRequest,
    GetMovieResponse,
    GetMoviesResponse,
)
from .viewmodels import Movie as MovieViewModel
from .viewmodels import UpdateMovieRequest, UpdateMoviesRequest


class BaseController(APIController):
    @staticmethod
    def get_dict_from_list(pydantic_models):
        if type(pydantic_models) is not list:
            raise Exception("List needed")
        return [m.dict() for m in pydantic_models]


class MoviesController(BaseController):
    """This controller is for list actions or create new one"""

    def __init__(self, **kwargs):
        # TODO register the service instance somewhere!
        self.movie_svc = MovieService()
        super().__init__(**kwargs)

    def get(self):
        search_term = self.request.query_params.get('title')
        movies_dm = self.movie_svc.get_movies(search_term)
        movies_vm = [mapper.to(MovieViewModel).map(m) for m in movies_dm]
        response = GetMoviesResponse(movies=movies_vm)
        return JsonResponse(response.dict(), safe=False)

    @strong_type(request_position=1, argument_name="create_request")
    def post(self, request, create_request: CreateMoviesRequest, format=None):
        # Map View Model to Domain Models
        movies_domain = [
            mapper.to(MovieDomainModel).map(m) for m in create_request.movies
        ]
        created_movies = self.movie_svc.create_movies(movies_domain)
        response = GetMoviesResponse(movies=created_movies)
        return JsonResponse(response.dict(), safe=False)

    # TODO here we can add bulk update with a put method


class MovieController(BaseController):
    """This controller is for single item actions"""

    def __init__(self, **kwargs):
        # TODO register the service instance somewhere!
        self.movie_svc = MovieService()
        super().__init__(**kwargs)

    def get(self, request, id, format=None):
        movie_dm = self.movie_svc.get_movie(id)
        movie_vm = mapper.to(MovieViewModel).map(movie_dm)
        response = GetMovieResponse(movie=movie_vm)
        return JsonResponse(response.dict())

    @strong_type()
    def put(self, request, id, model: UpdateMovieRequest, format=None):
        # Map View Model to Domain Models
        movie_dm = mapper.to(MovieDomainModel).map(model.movie)
        self.movie_svc.update_movie(movie_dm)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, id, format=None):
        self.movie_svc.delete_movie(id)
        return Response(status=status.HTTP_204_NO_CONTENT)
