from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models


class AddPerson(forms.ModelForm):
    CHOICES=(('Мужской','Мужской'), ('Женский','Женский'))
    gender = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'mb-2', 'type': 'radio'}))
    class Meta:
        model = models.Person
        fields = ['surname', 'name', 'patronymic', 'gender', 'birthday', 'birthplace', 'relation']
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Фамилия'}),
            'name': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Имя'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Отчество'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input mb-2', 'type': 'radio'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Дата рождения'}),
            'birthplace': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Место рождения'}),
            'relation': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Степень родства'})
        }


class AddResearch(forms.ModelForm):


    class Meta:
        model = models.Research
        fields = ['initiator_post', 'initiator_department', 'initiator_rank',
        'initiator_surname', 'initiator_name', 'initiator_patronymic', 'executor_post',
        'executor_department', 'executor_rank', 'executor_surname', 'executor_name',
        'executor_patronymic', 'event_number', 'formation_date', 'article', 'plot',
        'incident_date', 'address', 'relative_search']
        widgets = dict(
            initiator_post = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Должность'}),
            initiator_department = forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': 'Подразделение', 'rows': 4}),
            initiator_rank = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Специальное звание'}),
            initiator_surname = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            initiator_name = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            initiator_patronymic = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'}),
            executor_post = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Должность'}),
            executor_department = forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': 'Подразделение', 'rows': 4}),
            executor_rank = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Специальное звание'}),
            executor_surname = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            executor_name = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            executor_patronymic = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'}),
            event_number = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Номер материала (с указанием категории: у/д, РД, КУСП и т.д.)'}),
            formation_date = forms.DateInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Дата формирования'}),
            article = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'ст. УК РФ'}),
            plot = forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': 'Обстоятельства', 'rows': 8}),
            incident_date = forms.DateInput(attrs={'class': 'form-control date mb-2', 'placeholder': 'Дата происшествия'}),
            address = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Адрес места происшествия'}),
            relative_search = forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'})
        )


class RegisterForm(forms.ModelForm):
    # def clean(self):
    #     super().clean()
    #     errors = {}
    #     if not isinstance(self.cleaned_data['reg_number'], int) or self.cleaned_data['reg_number'] < 0:
    #         errors['reg_number'] = ValidationError(f"{self.cleaned_data['reg_number']} недопустимое значение")
    #     if self.cleaned_data['reg_number'] and self.cleaned_data['reg_date'] and not models.Research.verify_registration(self.cleaned_data['reg_number'], self.cleaned_data['reg_date']):
    #         errors['reg_number'] = ValidationError(f"Номер {self.cleaned_data['reg_number']} уже существует за годом {self.cleaned_data['reg_date'].year}")
    #     if errors:
    #         raise ValidationError(errors)
        
    
    class Meta:
        model = models.Research
        fields = ['reg_number', 'reg_date']
        widgets = dict(
            reg_number = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Номер'}),
            reg_date = forms.DateInput(attrs={'class': 'form-control date mb-2', 'placeholder': 'Дата регистрации'})
        )
