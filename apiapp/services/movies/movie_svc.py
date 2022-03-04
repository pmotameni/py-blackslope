from apiapp.repositories.movies import Movie as MovieDTO
from apiapp.repositories.movies import MovieRepository

from .domainmodels import Movie as MovieDomainModel

from automapper import mapper


class MovieService:
    def __init__(self):
        # TODO register the service instance some where!
        #       we do not need to recreate this everytime
        self.movie_repo = MovieRepository()

    def create_movies(self, movies: MovieDomainModel) -> list[MovieDomainModel]:
        movies_dto = [mapper.to(MovieDTO).map(m) for m in movies]
        created_movies = self.movie_repo.create_movies(movies_dto)
        return [mapper.to(MovieDomainModel).map(m) for m in created_movies]

    def delete_movie(self, id: str) -> None:
        self.movie_repo.delete_movie(id)

    def get_movie(self, id: str) -> MovieDomainModel:
        """Returns single movie"""
        movie_dto = self.movie_repo.get_movie(id)
        return mapper.to(MovieDomainModel).map(movie_dto)

    def get_movies(self, search_term: str) -> list[MovieDomainModel]:
        """'Returns list of movies"""
        movies_dto = self.movie_repo.get_movies()
        return [mapper.to(MovieDomainModel).map(m) for m in movies_dto]

    def update_movie(self, movie: MovieDomainModel) -> None:
        """Update single multiple movie"""
        movie_dto = mapper.to(MovieDTO).map(movie)
        self.movie_repo.update_movie(movie_dto)
        return

    def search_movies(self, title: str) -> list[MovieDomainModel]:
        """This is a simple search by title"""
        movies_dto = self.movie_repo.search_movies(title)
        return [mapper.to(MovieDomainModel).map(m) for m in movies_dto]
