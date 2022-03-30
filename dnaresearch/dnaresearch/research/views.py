from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from . import forms
from .services import *
from . import models


class Researches(ListView):
    model = models.Research
    template_name = 'research/research.html'
    context_object_name = 'researches'


class Research(DetailView):
    model = models.Research
    template_name = 'research/research_info.html'


class Persons(ListView):
    model = models.Person
    template_name = 'research/all_persons.html'
    context_object_name = 'persons'


class Person(DetailView):
    model = models.Person
    template_name = 'research/research.html'


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
        form = forms.AddPerson(request.POST)
        if form.is_valid():
            try:
                models.Person.objects.create(**form.cleaned_data, research_id=research_id)
                return redirect('persons', research_id)
            except:
                form.add_error(None, 'Ошибка добавления')
    else:
        form = forms.AddPerson()
    path = reverse('add_person', kwargs={'research_id': research_id})
    return render(request, 'research/add_person.html', {'form': form, 'path': path})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
