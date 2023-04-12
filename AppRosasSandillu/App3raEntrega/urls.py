from django.urls import path
from .views import BookListView, MovieListView, MusicListView, book_create, movie_create, music_create

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('music/', MusicListView.as_view(), name='music-list'),
    path('books/create/', book_create, name='book-create'),
    path('movies/create/', movie_create, name='movie-create'),
    path('music/create/', music_create, name='music-create'),
]