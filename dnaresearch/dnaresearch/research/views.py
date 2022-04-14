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
    template_name = 'research/persons.html'
    context_object_name = 'persons'

    def get_queryset(self):
        return get_person_by_research_id(research_id=self.kwargs['research_id'])


class Person(DetailView):
    model = models.Person
    template_name = 'research/person_detail.html'
    pk_url_kwarg = 'person_id'


class PersonDelete(DeleteView):
    model = models.Person
    pk_url_kwarg = 'person_id'

    def get_success_url(self):
        research_id = self.kwargs['research_id']
        return reverse_lazy('persons', kwargs={'research_id': research_id})


class AllPersons(ListView):
    model = models.Person
    template_name = 'research/all_persons.html'
    context_object_name = 'persons'


class PersonForm(CreateView):
    model = models.Person
    form_class = forms.AddPerson
    template_name = 'research/person_form.html'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.research_id = self.kwargs['research_id']
        fields.save()
        return super().form_valid(form)

    def get_success_url(self):
        research_id = self.kwargs['research_id']
        return reverse_lazy('persons', kwargs={'research_id': research_id})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
