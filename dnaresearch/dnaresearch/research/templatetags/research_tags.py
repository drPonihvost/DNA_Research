from django import template
from research import models
from django.urls import reverse

register = template.Library()


@register.simple_tag()
def get_research(research_id=None):
    if research_id:
        return models.Person.objects.filter(research_id=research_id)
    else:
        return models.Person.objects.all()


@register.simple_tag()
def check_related(research_id):
    return models.Research.objects.get(pk=research_id).relative_search


@register.simple_tag()
def get_person(research_id=None):
    if not research_id:
        return models.Person.objects.all()
    else:
        return models.Person.objects.filter(research_id=research_id)


@register.simple_tag()
def get_person_count(research_id):
    return models.Person.objects.filter(research_id=research_id).count()


@register.simple_tag()
def get_export_url(param):
    param=[1,2,3]
    if isinstance(param, int):
        url = reverse('research_export') + f'?research_id={param}'
    elif isinstance(param, list):
        param = [f'research_id={i}' for i in param]
        url = reverse('research_export') + f'?{param}'
    print(url)
    return reverse('research_export', kwargs={'research': [param]})

