from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .foms import AddPerson
from .services import *


def register(request):
    return render(request, 'research/research.html')


def research(request, research_id):
    return render(request, 'research/base.html', {'title': f'Исследование № {research_id}'})


def persons(request, research_id):
    context = {
        'research_id': research_id
    }
    return render(request, 'research/persons.html', context=context)


def all_persons(request):
    context = {
        'persons': get_all_persons()
    }
    return render(request, 'research/all_persons.html', context=context)


def add_person(request):
    form = AddPerson()
    return render(request, 'research/add_person.html', {'form': form})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

