
from django.shortcuts import render,redirect
from .models import Movie
from .forms import Movie_form
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method =='POST':
        movie_form = Movie_form(request.POST, request.FILES)
        if movie_form.is_valid():
            movie_form.save() 
            messages.success(request,('Your movie was successfully added')) 
        else:
            messages.error(request,('Error saving form'))
        
        return redirect('add_movie')
    
    movie_form = Movie_form()
    movies = Movie.objects.all()
    
    return render(request, 'main/add_movie.html', {'movie_form':movie_form, 'movies':movies})
            
  

def inicio(request):
    return render(request,'main/movies.html',{'movies':Movie.objects.all()})

def base(request):
    return render(request,'main/base.html')

