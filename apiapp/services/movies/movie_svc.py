from automapper import mapper

from apiapp.repositories.movies import Movie as MovieDTO
from apiapp.repositories.movies import MovieRepository

from .domainmodels import Movie as MovieDomainModel


class MovieService:
    def __init__(self):
        # TODO register the service instance some where!
        #       we do not need to recreate this everytime
        self.movie_repo = MovieRepository()

    def create_movies(self, movies: MovieDomainModel) -> list[MovieDomainModel]:
        """Create single movies"""
        movies_dto = [mapper.to(MovieDTO).map(m) for m in movies]
        created_movies = self.movie_repo.create_movies(movies_dto)
        return [mapper.to(MovieDomainModel).map(m) for m in created_movies]

    def delete_movie(self, id: str) -> None:
        """Delete single movie"""
        self.movie_repo.delete_movie(id)

    def get_movie(self, id: str) -> MovieDomainModel:
        """Returns single movie"""
        movie_dto = self.movie_repo.get_movie(id)
        return mapper.to(MovieDomainModel).map(movie_dto)

    def get_movies(self, search_term: str = None) -> list[MovieDomainModel]:
        """'Returns list of movies"""
        movies_dto = (
            self.movie_repo.search_movies(search_term)
            if search_term
            else self.movie_repo.get_movies()
        )
        return [mapper.to(MovieDomainModel).map(m) for m in movies_dto]

    def update_movie(self, movie: MovieDomainModel) -> None:
        """Update single multiple movie"""
        movie_dto = mapper.to(MovieDTO).map(movie)
        self.movie_repo.update_movie(movie_dto)
