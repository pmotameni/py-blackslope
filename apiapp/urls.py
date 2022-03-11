from django.urls import path

from apiapp.operations.movies import MovieController, MoviesController
from apiapp.services.movies import MovieService
from ioc.bootstrapper import Bootstrapper

container = Bootstrapper().bootstrap()

urlpatterns = [
    path(
        "movies/", MoviesController().as_view(movie_svc=container.resolve(MovieService))
    ),
    path(
        "movies/<int:id>/",
        MovieController().as_view(movie_svc=container.resolve(MovieService)),
    ),
]

# urlpatterns = [
#     path("movies/", MoviesController.as_view()),
#     path("movies/<int:id>/", MovieController.as_view()),
# ]
