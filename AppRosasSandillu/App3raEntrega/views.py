from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Libro, Pelicula, Musica
from .forms import LibroForm, PeliculaForm, MusicaForm

class BookListView(ListView):
    model = Libro
    template_name = 'libro_list.html'

class MovieListView(ListView):
    model = Pelicula
    template_name = 'pelicula_list.html'

class MusicListView(ListView):
    model = Musica
    template_name = 'musica_list.html'

def book_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LibroForm()
    return render(request, 'libro_form.html', {'form': form})

def movie_create(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PeliculaForm()
    return render(request, 'pelicula_form.html', {'form': form})

def music_create(request):
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MusicaForm()
    return render(request, 'musica_form.html', {'form': form})