from django import forms
from . import models


GENDER_MALE = 1
GENDER_FEMALE = 0
CHOICE_GENDER = ((GENDER_MALE, 'Мужской'), (GENDER_FEMALE, 'Женский'))


class AddPerson(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ['surname', 'name', 'patronymic', 'male', 'birthday', 'birthplace', 'relation']
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'male': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'input-type': 'text'}),
            'birthplace': forms.TextInput(attrs={'class': 'form-control'}),
            'relation': forms.TextInput(attrs={'class': 'form-control'})
        }


class AddResearch(forms.ModelForm):
    class Meta:
        model = models.Research
        fields = [
            'reg_number',
            'initiator_department',
            'initiator_post',
            'initiator_rank',
            'initiator_surname',
            'initiator_name',
            'initiator_patronymic',
            'executor_department',
            'executor_post',
            'executor_rank',
            'executor_surname',
            'executor_name',
            'executor_patronymic',
            'event_number',
            'formation_date',
            'article',
            'plot',
            'incident_date',
            'address',
            'relative_search',
            'reg_date'
        ]
        widgets = dict(
            reg_number = forms.TextInput(attrs={'class': 'form-control'}),
            initiator_department = forms.TextInput(attrs={'class': 'form-control'}),
            initiator_post = forms.TextInput(attrs={'class': 'form-control'}),
            initiator_rank = forms.TextInput(attrs={'class': 'form-control'}),
            initiator_surname = forms.TextInput(attrs={'class': 'form-control'}),
            initiator_name = forms.TextInput(attrs={'class': 'form-control'}),
            initiator_patronymic = forms.TextInput(attrs={'class': 'form-control'}),
            executor_department = forms.TextInput(attrs={'class': 'form-control'}),
            executor_post = forms.TextInput(attrs={'class': 'form-control'}),
            executor_rank = forms.TextInput(attrs={'class': 'form-control'}),
            executor_surname = forms.TextInput(attrs={'class': 'form-control'}),
            executor_name = forms.TextInput(attrs={'class': 'form-control'}),
            executor_patronymic = forms.TextInput(attrs={'class': 'form-control'}),
            event_number = forms.TextInput(attrs={'class': 'form-control'}),
            formation_date = forms.DateInput(attrs={'class': 'form-control', 'input-type': 'text'}),
            article = forms.TextInput(attrs={'class': 'form-control'}),
            plot = forms.TextInput(attrs={'class': 'form-control'}),
            incident_date = forms.DateInput(attrs={'class': 'form-control', 'input-type': 'text'}),
            address = forms.TextInput(attrs={'class': 'form-control'}),
            relative_search = forms.TextInput(attrs={'class': 'form-control'}),
            reg_date = forms.DateInput(attrs={'class': 'form-control', 'input-type': 'text'})
        )
