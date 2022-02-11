from django.urls import path

from apiapp.operations.movies import views

urlpatterns = [
    path("movies/", views.MoviesController.as_view()),
    path("movies/<int:id>/", views.MovieController.as_view()),
]
