from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . import forms
from .services import *
from . import models

# Research Mixin
class ResearchMixin:
    model = models.Research


class ResearchSingleMixin(ResearchMixin):
    pk_url_kwarg = 'research_id'


class ResearchListMixin(ResearchMixin):
    context_object_name = 'researches'


class ResearchFormMixin(ResearchSingleMixin):
    form_class = forms.AddResearch
    success_url = reverse_lazy('register')


# Research ListObject
class Researches(ResearchListMixin, ListView):
    template_name = 'research/research.html'


# Research SingleObject
class Research(ResearchSingleMixin, DetailView):
    template_name = 'research/research_detail.html'  


class ResearchForm(ResearchFormMixin, CreateView):
    template_name = 'research/research_form.html'


class ResearchUpdateForm(ResearchFormMixin, UpdateView):
    template_name = 'research/research_form.html'


class ResearchRegister(ResearchFormMixin, UpdateView):
    template_name = 'research/research_register.html'
    form_class = forms.RegisterForm


class ResearchDeleteForm(ResearchFormMixin, DeleteView):
    def get_success_url(self):
        return reverse_lazy('register')


# Person
# Person Mixins
class PersonMixin:
    model = models.Person


class PersonSingleMixin(PersonMixin):
    pk_url_kwarg = 'person_id'


class PersonListMixin(PersonMixin):
    context_object_name = 'persons'


class PersonRedirectMixin(PersonSingleMixin):
    def get_success_url(self):
        return reverse_lazy('persons', kwargs={'research_id': self.kwargs['research_id']})


class PersonFormMixin(PersonRedirectMixin):
    form_class = forms.AddPerson
    template_name = 'research/person_form.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['check_related'] = check_related(self.kwargs['research_id'])
        return context


# Person ListObject
class AllPersons(PersonListMixin, ListView):
    template_name = 'research/all_persons.html'


class Persons(PersonListMixin, ListView):
    template_name = 'research/persons.html'

    def get_queryset(self):
        return get_person_by_research_id(research_id=self.kwargs['research_id'])


# Person SingleObject
class Person(PersonSingleMixin, DetailView):
    template_name = 'research/person_detail.html'


class PersonForm(PersonFormMixin, CreateView):

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.research_id = self.kwargs['research_id']
        fields.save()
        return super().form_valid(form)


class PersonUpdate(PersonFormMixin, UpdateView):
    pass


class PersonDelete(PersonRedirectMixin, DeleteView):
    pass


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
