from django.urls import path

from .views import *

urlpatterns = [
    path('research/all', Researches.as_view(), name='register'),
    path('research/<int:research_id>', Research.as_view(), name='research_detail'),
    path('research/<int:research_id>/person', persons, name='persons'),
    path('research/<int:research_id>/person/<int:person_id>', Person.as_view(), name='person'),
    path('research/person/all', Persons.as_view(), name='all_persons'),
    path('research/<int:research_id>/person/add', add_person, name='add_person')
]
