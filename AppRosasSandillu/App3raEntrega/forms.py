from django import forms
from .models import Libro, Pelicula, Musica

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'autor', 'descripcion')

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('titulo', 'director', 'descripcion')

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ('titulo', 'artista', 'descripcion')

