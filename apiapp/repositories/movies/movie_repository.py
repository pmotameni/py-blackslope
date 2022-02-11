from .dtomodels import Movie


class MovieRepository:
    def create_movies(self, movies: list[Movie]):
        return Movie.objects.bulk_create(movies)

    def get_movies(self):
        return Movie.objects.all()

    def get_movie(self, id):
        return Movie.objects.get(id=id)

    def delete_movie(self, id):
        movie = Movie.objects.get(id=id)
        if movie:
            movie.delete()
        else:
            raise Exception(f"Could not find movie with {id}")

    def update_movie(self, movie):
        movie.save()
