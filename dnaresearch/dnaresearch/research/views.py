from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .foms import AddPerson
from .services import *

class ResearchRegister(ListView):
    model = Research
    template_name = 'research/research.html'


# def register(request):
#     return render(request, 'research/research.html')


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


def add_person(request, research_id):
    if request.method == 'POST':
        form = AddPerson(request.POST)
        if form.is_valid():
            try:
                Person.objects.create(**form.cleaned_data, research_id=research_id)
                return redirect('persons', research_id)
            except:
                form.add_error(None, 'Ошибка добавления')
    else:
        form = AddPerson()
    return render(request, 'research/add_person.html', {'form': form})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

