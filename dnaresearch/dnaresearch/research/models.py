from django.db import models
from django.urls import reverse



class CriminalArticles(models.Model):
    """Унифицированный список статей УК РФ"""
    article = models.CharField(max_length=1000, verbose_name='Статья УК РФ')

    def __str__(self):
        return self.article

    class Meta:
        db_table = 'Статьи УК РФ'
        verbose_name = 'Статьи УК РФ'
        verbose_name_plural = 'Статьи УК РФ'
        ordering = ['article']


class Research(models.Model):
    reg_number = models.IntegerField(blank=True, default=None, null=True)
    date_of_record = models.DateField(auto_now_add=True)
    initiator_department = models.TextField()
    initiator_post = models.TextField()
    initiator_rank = models.CharField(max_length=255)
    initiator_surname = models.CharField(max_length=255)
    initiator_name = models.CharField(max_length=255)
    initiator_patronymic = models.CharField(max_length=255)
    executor_department = models.TextField()
    executor_post = models.TextField()
    executor_rank = models.CharField(max_length=255)
    executor_surname = models.CharField(max_length=255)
    executor_name = models.CharField(max_length=255)
    executor_patronymic = models.CharField(max_length=255)
    event_number = models.CharField(max_length=255)
    formation_date = models.DateField()
    article = models.CharField(max_length=255, blank=True, null=True)
    plot = models.TextField(blank=True, default=None, null=True)
    incident_date = models.DateField(blank=True, default=None, null=True)
    address = models.TextField(blank=True, default=None, null=True)
    relative_search = models.BooleanField(default=False)
    reg_date = models.DateField(blank=True, default=None, null=True)

    class Meta:
        verbose_name = 'Исследования'
        verbose_name_plural = 'Исследования'

    def __str__(self):
        return self.reg_number

    def get_absolute_url(self):
        return reverse('research_detail', kwargs={'research_id': self.pk})

    def get_url_for_persons(self):
        return reverse('persons', kwargs={'research_id': self.pk})

    def get_url_for_research_update(self):
        return reverse('research_update_form', kwargs={'research_id': self.pk})

    def get_export_url(self):
        return reverse('research_export') + f'?research_id={self.pk}'


class Nationality(models.Model):
    name = models.CharField(max_length=255)
    group = models.CharField(max_length=255, blank=True, null=True, default=None)


class Person(models.Model):

    class Gender(models.TextChoices):
        MALE = 'Мужской'
        FEMALE = 'Женский'

    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    gender = models.CharField(max_length=7, choices=Gender.choices, default=Gender.MALE)
    birthday = models.DateField()
    birthplace = models.TextField()
    relation = models.CharField(max_length=255, blank=True, null=True, default=None)
    passport_series = models.CharField(max_length=6, blank=True, null=True, default=None)
    passport_number = models.CharField(max_length=4, blank=True, null=True, default=None)
    pasport_date_of_issue = models.DateField(blank=True, null=True, default=None)
    pasport_division_code = models.CharField(max_length=6, blank=True, null=True, default=None)
    pasport_division_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    inn = models.CharField(max_length=25, blank=True, null=True, default=None)
    snils = models.CharField(max_length=11, blank=True, null=True, default=None)
    victim = models.BooleanField(default=False, blank=True, null=True,)
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, blank=True, null=True)
    citizenship = models.CharField(max_length=255, blank=True, null=True, default=None)

    research = models.ForeignKey(Research, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Лица на проверку'
        verbose_name_plural = 'Лица на проверку'

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} {self.birthday} г.р.'

    def get_absolute_url(self):
        return reverse('person_detail', kwargs={'research_id': self.research.pk, 'person_id': self.pk})

    def get_url_for_update(self):
        return reverse('person_update', kwargs={'research_id': self.research.pk, 'person_id': self.pk})

    def get_url_for_delete(self):
        return reverse('person_delete', kwargs={'research_id': self.research.pk, 'person_id': self.pk})

    