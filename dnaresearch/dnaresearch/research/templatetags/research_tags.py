from django import template
from research import models

register = template.Library()


@register.simple_tag()
def get_all_research():
    return models.Research.objects.all()


@register.simple_tag()
def get_persons(research_id=None):
    if not research_id:
        return models.Person.objects.all()
    else:
        return models.Person.objects.filter(research_id=research_id)


@register.simple_tag()
def get_person_count(research_id):
    return models.Person.objects.filter(research_id=research_id).count()

