from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .services import *


def register(request):
    researches = get_all_research()
    return render(request, 'research/research.html', {'researches': researches})


def research(request, research_id):
    return render(request, 'research/base.html', {'title': f'Исследование № {research_id}'})


def persons(request, research_id):
    persons_ = get_person_by_research_id(research_id)
    context = {
        'research_id': research_id,
        'persons': persons_
    }
    return render(request, 'research/persons.html', context=context)


def all_persons(request):
    context = {
        'persons': get_all_persons()
    }
    return render(request, 'research/all_persons.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

