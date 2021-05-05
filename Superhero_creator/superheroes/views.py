from django.shortcuts import render
from django.http import HttpResponse
from .models import Superhero


def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


def detail(request, superhero_id):
    superhero = Superhero.objects.get(pk=superhero_id)
    context = {
        'superhero': superhero
    }
    return render(request, 'superheroes/detail.html', context)
