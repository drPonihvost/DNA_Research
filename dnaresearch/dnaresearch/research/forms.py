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


# class AddResearch(forms.ModelForm):
#     class Meta:
#         model = models.Research
#         fields = ['surname', 'name', 'patronymic', 'male', 'birthday', 'birthplace', 'relation']
#         widgets = {
#             'surname': forms.TextInput(attrs={'class': 'form-control'}),
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
#             'male': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#             'birthday': forms.DateInput(attrs={'class': 'form-control', 'input-type': 'text'}),
#             'birthplace': forms.TextInput(attrs={'class': 'form-control'}),
#             'relation': forms.TextInput(attrs={'class': 'form-control'})
#         }
