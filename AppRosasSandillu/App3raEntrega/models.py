from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    descripcion = models.TextField()

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    descripcion = models.TextField()

class Musica(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    descripcion = models.TextField()
    