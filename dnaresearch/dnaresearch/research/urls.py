from django.urls import path

from .forms import AddResearch

from .views import *

urlpatterns = [
    path('research/', Researches.as_view(), name='register'),
    path('research/add', ResearchForm.as_view(), name='research_form'),
    path('research/<int:research_id>', Research.as_view(), name='research_detail'),
    path('research/<int:research_id>/edit', ResearchUpdateForm.as_view(), name='research_update_form'),
    path('research/<int:research_id>/remove', ResearchDeleteForm.as_view(), name='research_delete'),
    path('research/<int:research_id>/person', persons, name='persons'),
    path('research/<int:research_id>/person/<int:person_id>', Person.as_view(), name='person'),
    path('research/person', Persons.as_view(), name='all_persons'),
    path('research/<int:research_id>/person/add', add_person, name='add_person')
]
