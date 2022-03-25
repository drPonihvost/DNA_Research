from django.urls import path

from .views import *

urlpatterns = [
    path('register', ResearchRegister.as_view(), name='register'),
    path('research/<int:research_id>', research, name='research'),
    path('research/<int:research_id>/persons', persons, name='persons'),
    path('research/all_persons', AllPersons.as_view(), name='all_persons'),
    path('research/<int:research_id>/persons/add_person', AddPerson.as_view(), name='add_person')
]
