from .dtomodels import Movie


class MovieRepository:
    @staticmethod
    def create_movies(movies: list[Movie]) -> list[Movie]:
        return Movie.objects.bulk_create(movies)

    @staticmethod
    def get_movies() -> list[Movie]:
        return Movie.objects.all()

    @staticmethod
    def get_movie(id: str) -> Movie:
        return Movie.objects.get(id=id)

    @staticmethod
    def delete_movie(id: str) -> None:
        movie = Movie.objects.get(id=id)
        if movie:
            movie.delete()
        else:
            raise Exception(f"Could not find movie with {id}")

    @staticmethod
    def update_movie(movie: Movie) -> None:
        movie.save()

    @staticmethod
    def search_movies(title: str):
        return Movie.objects.filter(title__contains=title)
