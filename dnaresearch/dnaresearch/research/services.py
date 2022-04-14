from .models import *


def get_all_research():
    return Research.objects.all()


def get_research_by_id(research_id):
    return Research.objects.get(pk=research_id)


def check_related(research_id):
    return Research.objects.get(pk=research_id).relative_search


def get_person_by_research_id(research_id):
    return Person.objects.filter(research_id=research_id)


def get_all_persons():
    return Person.objects.all()