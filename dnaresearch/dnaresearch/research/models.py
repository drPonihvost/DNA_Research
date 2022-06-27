from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.models import User


class CriminalArticles(models.Model):
    """Унифицированный список статей УК РФ"""
    number = models.CharField(max_length=10, blank=True, default='', verbose_name='Статья')
    description = models.CharField(max_length=1000, verbose_name='Описание')

    class Meta:
        verbose_name = 'Статья УК РФ'
        verbose_name_plural = 'Статьи УК РФ'
        ordering = ['number']

    def __str__(self):
        return str(self.number)

    


class Research(models.Model):
    reg_number = models.IntegerField(blank=True, default=None, null=True, verbose_name='Регистрационный номер')
    date_of_record = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    initiator_department = models.TextField(verbose_name='Подразделение (Инициатор)')
    initiator_post = models.TextField(verbose_name='Должность (Инициатор)')
    initiator_rank = models.CharField(max_length=255, verbose_name='Сп. звание (Инициатор)')
    initiator_surname = models.CharField(max_length=255, verbose_name='Фамилия (Инициатор)')
    initiator_name = models.CharField(max_length=255, verbose_name='Имя (Инициатор)')
    initiator_patronymic = models.CharField(max_length=255, verbose_name='Отчество (Инициатор)')
    executor_department = models.TextField(verbose_name='Подразделение (Исполнитель)')
    executor_post = models.TextField(verbose_name='Должность (Исполнитель)')
    executor_rank = models.CharField(max_length=255, verbose_name='Сп. звание (Исполнитель)')
    executor_surname = models.CharField(max_length=255, verbose_name='Фамилия (Исполнитель)')
    executor_name = models.CharField(max_length=255, verbose_name='Имя (Исполнитель)')
    executor_patronymic = models.CharField(max_length=255, verbose_name='Отчество (Исполнитель)')
    event_number = models.CharField(max_length=255, verbose_name='Материалы')
    formation_date = models.DateField(verbose_name='Дата регистрации материалов')
    article = models.CharField(max_length=255, blank=True, null=True, verbose_name='Статья УК РФ')
    plot = models.TextField(blank=True, default=None, null=True, verbose_name='Событие')
    incident_date = models.DateField(blank=True, default=None, null=True, verbose_name='Дата происшествия')
    address = models.TextField(blank=True, default=None, null=True, verbose_name='Адрес места происшествия')
    relative_search = models.BooleanField(default=False, verbose_name='Родственный поиск')
    reg_date = models.DateField(blank=True, default=None, null=True, verbose_name='Дата регистрации')
    user = models.ForeignKey(User,blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Принял эксперт')

    class Meta:
        verbose_name = 'Исследования'
        verbose_name_plural = 'Исследования'
        ordering = ['-date_of_record']
        constraints = [
            models.UniqueConstraint(fields=['reg_number', 'reg_date'], name='unique research'),
        ]

    def clean(self):
        errors = {}
        if self.reg_number is not None and self.reg_date is not None:
            if not isinstance(self.reg_number, int) or self.reg_number < 0:
                errors['reg_number'] = ValidationError(_(f'{self.reg_number} недопустимое значение'), params={'value': self.reg_number})
            if self.verify_registration():
                errors['reg_number'] = ValidationError(_(f'Номер {self.reg_number} уже существует за годом {self.reg_date.year}'), params={'value': self.reg_number})
        elif self.reg_number is None and self.reg_date is not None:
            errors['reg_number'] = ValidationError(_('Невозможно зарегистрировать без номера'), params={'value': self.reg_number})
        elif self.reg_date is None and self.reg_number is not None:
            errors['reg_date'] = ValidationError(_('Невозможно зарегистрировать без даты'), params={'value': self.reg_date})
        
        if self.formation_date < self.incident_date:
            errors['formation_date'] = ValidationError(_('Дата формирования материалов не может быть раньше даты происшествия'), params={'value': self.reg_number})


        if errors:
            raise ValidationError(errors)

    def verify_registration(self):
        records = Research.objects.filter(reg_number=self.reg_number, reg_date__year=self.reg_date.year)
        if not records:
            return False
        elif len(records) == 1 and records[0].pk == self.pk:
            return False
        return True


    def __str__(self):
        return str(self.reg_number)

    def get_absolute_url(self):
        return reverse('research_detail', kwargs={'research_id': self.pk})

    def get_url_for_persons(self):
        return reverse('persons', kwargs={'research_id': self.pk})

    def get_url_for_research_update(self):
        return reverse('research_update_form', kwargs={'research_id': self.pk})

    def get_export_url(self):
        return reverse('research_export') + f'?research_id={self.pk}'


class Nationality(models.Model):
    name = models.CharField(max_length=255, verbose_name='Национальность')
    group = models.CharField(max_length=255, blank=True, null=True, default=None, verbose_name='Группа')

    class Meta:
        verbose_name = 'Национальность'
        verbose_name_plural = 'Национальность'
        ordering = ['pk']


class Person(models.Model):

    class Gender(models.TextChoices):
        MALE = 'Мужской'
        FEMALE = 'Женский'

    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    gender = models.CharField(max_length=7, choices=Gender.choices, default=Gender.MALE, verbose_name='Пол')
    birthday = models.DateField(verbose_name='Дата рождения')
    birthplace = models.TextField(blank=True, null=True, default='Не установлено', verbose_name='Место рождения')
    relation = models.CharField(max_length=255, blank=True, null=True, default=None, verbose_name='Степень родства')
    passport_series = models.CharField(max_length=6, blank=True, null=True, default=None, verbose_name='Серия паспорта')
    passport_number = models.CharField(max_length=4, blank=True, null=True, default=None, verbose_name='Номер паспорта')
    pasport_date_of_issue = models.DateField(blank=True, null=True, default=None, verbose_name='Дата выдачи')
    pasport_division_code = models.CharField(max_length=6, blank=True, null=True, default=None, verbose_name='Код подразделения')
    pasport_division_name = models.CharField(max_length=255, blank=True, null=True, default=None, verbose_name='Подразделение')
    inn = models.CharField(max_length=25, blank=True, null=True, default=None, verbose_name='ИНН')
    snils = models.CharField(max_length=11, blank=True, null=True, default=None, verbose_name='СНИЛС')
    victim = models.BooleanField(default=False, blank=True, null=True, verbose_name='Потерпевший')
    citizenship = models.CharField(max_length=255, blank=True, null=True, default=None, verbose_name='Гражданство')

    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Национальность')
    research = models.ForeignKey(Research, on_delete=models.CASCADE, blank=True, verbose_name='Исследование')

    class Meta:
        verbose_name = 'Лица на проверку'
        verbose_name_plural = 'Лица на проверку'
        ordering = ['pk']

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} {self.birthday} г.р.'

    def get_absolute_url(self):
        return reverse('person_detail', kwargs={'research_id': self.research.pk, 'person_id': self.pk})

    def get_url_for_update(self):
        return reverse('person_update', kwargs={'research_id': self.research.pk, 'person_id': self.pk})

    def get_url_for_delete(self):
        return reverse('person_delete', kwargs={'research_id': self.research.pk, 'person_id': self.pk})

