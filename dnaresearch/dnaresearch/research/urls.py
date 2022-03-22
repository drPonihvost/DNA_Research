from django.urls import path

from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('research/<int:research_id>', research, name='research'),
    path('research/<int:research_id>/persons', persons, name='persons'),
    path('research/all_persons', all_persons, name='all_persons')
]
