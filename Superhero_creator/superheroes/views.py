from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name, alter_ego_name=alter_ego, primary_ability=primary_ability,
                                  secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def update(request, superhero_id):
    superhero = Superhero.objects.get(pk=superhero_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        superhero.name = name
        superhero.alter_ego_name = alter_ego
        superhero.primary_ability = primary_ability
        superhero.secondary_ability = secondary_ability
        superhero.category = catchphrase
        superhero.save()
        return HttpResponseRedirect(f'/superheroes/display/{superhero.id}')
    else:
        return render(request, 'superheroes/index.html')


def delete(request, superhero_id):
    superhero = Superhero.objects.get(pk=superhero_id)
    superhero.delete()
    return HttpResponseRedirect(reverse('superheroes:index'))
