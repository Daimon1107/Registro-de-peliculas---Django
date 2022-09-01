from tkinter import Label
from django.db import models

# Create your models here.

class Movie(models.Model):
    title  = models.CharField(max_length=100,verbose_name='Título')
    release_year = models.IntegerField(verbose_name='Año de estreno')
    director  = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters_movie',verbose_name='Portada')
    plot = models.TextField(verbose_name='Sinopsis',)
    
    def __str__(self):
        return self.title
    
    