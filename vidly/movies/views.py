from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    m = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': m})

    # try:
    #     m = Movie.objects.get(id=movie_id)
    #     return render(request, 'movies/detail.html', {'movie': m})
    # except Movie.DoesNotExist:
    #     raise Http404


def add(request):
    return render(request, 'movies/add.html')


def delete(request, movie_id):
    m = get_object_or_404(Movie, id=movie_id)

    m.delete()
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})
