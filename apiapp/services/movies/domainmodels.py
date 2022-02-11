from datetime import date

from pydantic import BaseModel


class Movie(BaseModel):
    id: str | None
    title: str
    description: str | None
    release_date: date | None
