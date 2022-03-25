from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from . import forms
from .services import *


class ResearchRegister(ListView):
    model = Research
    template_name = 'research/research.html'
    context_object_name = 'researches'


class AllPersons(ListView):
    model = Person
    template_name = 'research/all_persons.html'
    context_object_name = 'persons'


class Research(DetailView):
    model = Research
    template_name = 'research/research.html'


class AddPerson(CreateView):
    def __init__(self, research_id):
        super(AddPerson, self).__init__()
        form_class = forms.AddPerson
        template_name = 'research/add_person.html'
        extra_context = research_id


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


# def add_person(request, research_id):
#     if request.method == 'POST':
#         form = AddPerson(request.POST)
#         if form.is_valid():
#             try:
#                 Person.objects.create(**form.cleaned_data, research_id=research_id)
#                 return redirect('persons', research_id)
#             except:
#                 form.add_error(None, 'Ошибка добавления')
#     else:
#         form = AddPerson()
#     path = reverse('add_person', kwargs={'research_id': research_id})
#     return render(request, 'research/add_person.html', {'form': form, 'path': path})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

