from django.shortcuts import render
from .models import director, pelicula, genre

# Create your views here.
def index(request):
    
    num_films = pelicula.objects.all().count()
    num_directors = director.objects.all().count()
    num_genres = genre.objects.all().count()

    context = {
        'num_films': num_films,
        'num_directors': num_directors,
        'num_genres': num_genres,
    }

    return render(request, 'index.html', context)
