from socket import fromshare
from django import forms
from .models import Movie


class Movie_form(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title','release_year','director','poster','plot')