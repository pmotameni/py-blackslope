from apiapp.repositories.movies import Movie as MovieDTO
from apiapp.repositories.movies import MovieRepository

from .domainmodels import Movie as MovieDomainModel


class MovieService:
    def __init__(self):
        # TODO register the service instance somewhere!
        #       we do not to recreate this everytime
        self.movie_repo = MovieRepository()

    def create_movies(self, movies):
        movies_dto = [self.map_movie_domain_to_dto(m) for m in movies]
        created_movies = self.movie_repo.create_movies(movies_dto)
        return [self.map_movie_dto_to_domain(m) for m in created_movies]

    def delete_movie(self, id):
        self.movie_repo.delete_movie(id)

    def get_movie(self, id):
        """Returns single movie"""
        movie_dto = self.movie_repo.get_movie(id)
        return self.map_movie_dto_to_domain(movie_dto)

    def get_movies(self):
        """'Returns list of movies"""
        movies_dto = self.movie_repo.get_movies()
        return [self.map_movie_dto_to_domain(m) for m in movies_dto]

    def update_movie(self, movie):
        """Update single multiple movie"""
        movie_dto = self.map_movie_domain_to_dto(movie, has_id=True)
        self.movie_repo.update_movie(movie_dto)
        return

    def does_movie_exist(self, title):
        """This is a simple search by title"""
        pass

    @staticmethod
    def map_movie_dto_to_domain(movie) -> MovieDomainModel:
        # TODO this is temporary need to create def for automapper
        return MovieDomainModel(
            id=movie.id,
            title=movie.title,
            description=movie.description,
            release_date=movie.release_date,
        )

    @staticmethod
    def map_movie_domain_to_dto(movie, has_id=False) -> MovieDTO:
        # TODO this is temporary need to create def for automapper
        dto = MovieDTO(
            title=movie.title,
            description=movie.description,
            release_date=movie.release_date,
        )
        if has_id:
            dto.id = movie.id
        return dto
