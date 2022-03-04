from .dtomodels import Movie


class MovieRepository:
    def create_movies(self, movies: list[Movie]) -> list[Movie]:
        return Movie.objects.bulk_create(movies)

    def get_movies(self) -> list[Movie]:
        return Movie.objects.all()

    def get_movie(self, id: str) -> Movie:
        return Movie.objects.get(id=id)

    def delete_movie(self, id: str) -> None:
        movie = Movie.objects.get(id=id)
        if movie:
            movie.delete()
        else:
            raise Exception(f"Could not find movie with {id}")

    def update_movie(self, movie: Movie) -> None:
        movie.save()

    def search_movies(self, title: str):
        return Movie.objects.filter(title__contains=title)
