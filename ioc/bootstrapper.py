from punq import Container

from apiapp.operations.movies import MovieController, MoviesController
from apiapp.repositories.movies import MovieRepository
from apiapp.services.movies import MovieService


class Bootstrapper:
    def bootstrap(self) -> Container:
        container = Container()
        container.register(MovieService)
        container.register(MovieRepository, instance=MovieRepository())

        return container
