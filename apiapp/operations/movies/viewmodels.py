from datetime import date

from pydantic import BaseModel


class Movie(BaseModel):
    id: str | None
    title: str
    description: str | None
    release_date: date | None


class CreateMovie(BaseModel):
    title: str
    description: str | None
    release_date: date | None


class CreateMovieRequest(BaseModel):
    movie: CreateMovie


class CreateMoviesRequest(BaseModel):
    movies: list[CreateMovie]


class UpdateMovieRequest(BaseModel):
    movie: Movie


class UpdateMoviesRequest(BaseModel):
    movies: list[Movie]


class GetMovieResponse(BaseModel):
    movie: Movie


class GetMoviesResponse(BaseModel):
    movies: list[Movie]
