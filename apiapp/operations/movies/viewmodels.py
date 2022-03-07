from datetime import date

from pydantic import BaseModel


class MovieViewModel(BaseModel):
    id: str | None
    title: str
    description: str | None
    release_date: date | None


class CreateMovieRequest(BaseModel):
    movie: MovieViewModel


class CreateMoviesRequest(BaseModel):
    movies: list[MovieViewModel]


class UpdateMovieRequest(BaseModel):
    movie: MovieViewModel


class UpdateMoviesRequest(BaseModel):
    movies: list[MovieViewModel]


class GetMovieResponse(BaseModel):
    movie: MovieViewModel


class GetMoviesResponse(BaseModel):
    movies: list[MovieViewModel]
