from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . import forms
from .services import *
from . import models


class Researches(ListView):
    model = models.Research
    template_name = 'research/research.html'
    context_object_name = 'researches'


class Research(DetailView):
    model = models.Research
    template_name = 'research/research_detail.html'
    pk_url_kwarg = 'research_id'


class ResearchViewMixin:
    model = models.Research
    form_class = forms.AddResearch
    success_url = reverse_lazy('register')


class ResearchForm(ResearchViewMixin, CreateView):
    template_name = 'research/research_form.html'


class ResearchUpdateForm(ResearchViewMixin, UpdateView):
    template_name = 'research/research.html'
    pk_url_kwarg = 'research_id' 


class ResearchRegister(ResearchViewMixin, UpdateView):
    template_name = 'research/research_register.html'
    form_class = forms.RegisterForm
    pk_url_kwarg = 'research_id' 


class ResearchDeleteForm(DeleteView):
    model = models.Research
    template_name = 'research/research.html'
    success_url = reverse_lazy('register')
    pk_url_kwarg = 'research_id'


class Persons(ListView):
    model = models.Person
    template_name = 'research/all_persons.html'
    context_object_name = 'persons'


class Person(DetailView):
    model = models.Person
    template_name = 'research/person_detail.html'
    pk_url_kwarg = 'person_id'



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

""" def add_research(request):
    if request.method == 'POST':
        form = forms.AddResearch(request.POST)
        if form.is_valid():
            try:
                models.Research.objects.create(**form.cleaned_data)
                return redirect('register')
            except:
                form.add_error(None, 'Ошибка добавления')
    else:
        form = forms.AddResearch()
    return render(request, 'research/research_form.html', {'form': form}) """


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
