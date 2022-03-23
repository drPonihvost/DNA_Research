from django import forms
from .models import *


class AddPerson(forms.Form):
    surname = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    patronymic = forms.CharField(max_length=255)
    male = forms.BooleanField()
    birthday = forms.DateField()
    birthplace = forms.DateField()
    relation = forms.CharField(max_length=255)
