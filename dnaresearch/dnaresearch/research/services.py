from .models import *


def get_all_research():
    return Research.objects.all()


def get_person_by_research_id(research_id):
    return Person.objects.filter(research_id=research_id)


def get_all_persons():
    return Person.objects.all()