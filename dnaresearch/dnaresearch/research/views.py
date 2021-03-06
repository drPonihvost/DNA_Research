import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from core.views import ErrorHandlingMixin, error_handling
from . import forms
from . import services
from . import models


# -------Research Mixin--------
class ResearchMixin(ErrorHandlingMixin, LoginRequiredMixin, PermissionRequiredMixin):
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
    permission_required = 'research.view_research'




# Research SingleObject
class Research(ResearchSingleMixin, DetailView):
    template_name = 'research/research_detail.html'
    permission_required = 'research.view_research'


class ResearchForm(ResearchFormMixin, CreateView):
    template_name = 'research/research_form.html'
    permission_required = 'research.add_research'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.user = self.request.user
        fields.save()
        return super().form_valid(form)


class ResearchUpdateForm(ResearchFormMixin, UpdateView):
    template_name = 'research/research_form.html'
    permission_required = 'research.change_research'


class ResearchRegister(ResearchFormMixin, UpdateView):
    template_name = 'research/research_register.html'
    form_class = forms.RegisterForm
    permission_required = 'research.change_research'


class ResearchDeleteForm(ResearchSingleMixin, DeleteView):
    success_url = reverse_lazy('register')
    permission_required = 'research.delete_research'


# Person
# Person Mixins
class PersonMixin(ErrorHandlingMixin, LoginRequiredMixin, PermissionRequiredMixin):
    model = models.Person
    permission_required = ('research.view_research', 'research.add_research', 'research.change_research', 'research.delete_research')


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
        context['check_related'] = services.check_related(self.kwargs['research_id'])
        return context


# Person ListObject
class AllPersons(PersonListMixin, ListView):
    template_name = 'research/all_persons.html'
    permission_required = 'research.view_research'


class Persons(PersonListMixin, ListView):
    template_name = 'research/persons.html'
    permission_required = 'research.view_research'

    def get_queryset(self):
        return services.get_person_by_research_id(research_id=self.kwargs['research_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['research_id'] = self.kwargs['research_id']
        return context
      

# Person SingleObject
class Person(PersonSingleMixin, DetailView):
    template_name = 'research/person_detail.html'
    permission_required = 'research.view_research'


class PersonForm(PersonFormMixin, CreateView):
    permission_required = 'research.add_research'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.research_id = self.kwargs['research_id']
        fields.save()
        return super().form_valid(form)


class PersonUpdate(PersonFormMixin, UpdateView):
    permission_required = 'research.change_research'


class PersonDelete(PersonRedirectMixin, DeleteView):
    permission_required = 'research.delete_research'


@error_handling
@login_required
def export_research(request):
    researches_id = (request.GET.get('research_id', None))
    if isinstance(researches_id, int):
        researches_id = list(researches_id)
    elif isinstance(researches_id, str):
        researches_id = researches_id.split(sep=',')
    else:
        return HttpResponseNotFound('<h1>???????????????? ???? ??????????????</h1>')
    
    export_file = ExportFile(researches_id)
    export_file.create_txt()
    path = ExportFile.FILE_NAME

    with open(path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
            return response


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>???????????????? ???? ??????????????</h1>')
