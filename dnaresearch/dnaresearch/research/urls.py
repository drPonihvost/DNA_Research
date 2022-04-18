from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('research/', Researches.as_view(), name='register'),
    path('research/add', ResearchForm.as_view(), name='research_form'),
    path('research/export', single_export, name='research_export'),
    path('research/<int:research_id>', Research.as_view(), name='research_detail'),
    path('research/<int:research_id>/edit', ResearchUpdateForm.as_view(), name='research_update_form'),
    path('research/<int:research_id>/remove', ResearchDeleteForm.as_view(), name='research_delete'),
    path('research/<int:research_id>/register', ResearchRegister.as_view(), name='research_register'),
    path('research/person', AllPersons.as_view(), name='all_persons'),
    path('research/<int:research_id>/person', Persons.as_view(), name='persons'),
    path('research/<int:research_id>/person/<int:person_id>', Person.as_view(), name='person_detail'),
    path('research/<int:research_id>/person/add', PersonForm.as_view(), name='person_form'),
    path('research/<int:research_id>/person/<int:person_id>/update', PersonUpdate.as_view(), name='person_update'),
    path('research/<int:research_id>/person/<int:person_id>/delete', PersonDelete.as_view(), name='person_delete'),
]
