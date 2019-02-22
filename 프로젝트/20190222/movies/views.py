from django.shortcuts import render, redirect
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.order_by('id')
    return render(request, 'movies/index.html', {'movies': movies})

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    movie = Movie()
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()
    
    return redirect('/movies/')
    
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/detail.html', {'movie': movie})
    
def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/edit.html', {'movie': movie})

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()
    
    return redirect(f'/movies/{ movie.pk }/')
    
    
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('/movies/')