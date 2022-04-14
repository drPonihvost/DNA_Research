from tkinter import N
from django import template
from research import models

register = template.Library()


@register.simple_tag()
def get_research(research_id=None):
    if research_id:
        return models.Person.objects.filter(research_id=research_id)
    else:
        return models.Person.objects.all()


@register.simple_tag()
def check_related(research_id):
    if models.Person.objects.get(research_id):
        return True
    return False


@register.simple_tag()
def get_person(research_id=None):
    if not research_id:
        return models.Person.objects.all()
    else:
        return models.Person.objects.filter(research_id=research_id)


@register.simple_tag()
def get_person_count(research_id):
    return models.Person.objects.filter(research_id=research_id).count()

