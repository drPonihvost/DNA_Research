from django import template
from research.models import *

register = template.Library()


@register.simple_tag()
def get_all_research():
    return Research.objects.all()


@register.simple_tag()
def get_persons(research_id=None):
    if not research_id:
        return Person.objects.all()
    else:
        return Person.objects.filter(research_id=research_id)

