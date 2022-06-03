from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.Researches.as_view(), name='register'),
    path('add', views.ResearchForm.as_view(), name='research_form'),
    path('export/', views.export_research, name='research_export'),
    path('<int:research_id>', views.Research.as_view(), name='research_detail'),
    path('<int:research_id>/edit', views.ResearchUpdateForm.as_view(), name='research_update_form'),
    path('<int:research_id>/remove', views.ResearchDeleteForm.as_view(), name='research_delete'),
    path('<int:research_id>/register', views.ResearchRegister.as_view(), name='research_register'),
    path('person', views.AllPersons.as_view(), name='all_persons'),
    path('<int:research_id>/person', views.Persons.as_view(), name='persons'),
    path('<int:research_id>/person/<int:person_id>', views.Person.as_view(), name='person_detail'),
    path('<int:research_id>/person/add', views.PersonForm.as_view(), name='person_form'),
    path('<int:research_id>/person/<int:person_id>/update', views.PersonUpdate.as_view(), name='person_update'),
    path('<int:research_id>/person/<int:person_id>/delete', views.PersonDelete.as_view(), name='person_delete'),
]
