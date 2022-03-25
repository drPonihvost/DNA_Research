from django.db import models
from django.urls import reverse


class Research(models.Model):
    reg_number = models.IntegerField(blank=True, default=None)
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
    article = models.CharField(max_length=255, blank=True)
    plot = models.TextField(blank=True, default=None)
    incident_date = models.DateField(blank=True, default=None)
    address = models.TextField(blank=True, default=None)
    relative_search = models.BooleanField(default=False)
    reg_date = models.DateField(blank=True, default=None)

    class Meta:
        verbose_name = 'Исследования'
        verbose_name_plural = 'Исследования'

    def __str__(self):
        return self.reg_number

    def get_absolute_url(self):
        return reverse('research', kwargs={'research_id': self.pk})


class Person(models.Model):
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    male = models.BooleanField()
    birthday = models.DateField()
    birthplace = models.TextField()
    relation = models.CharField(max_length=255, blank=True, null=True, default=None)

    research = models.ForeignKey(Research, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Лица на проверку'
        verbose_name_plural = 'Лица на проверку'

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} {self.birthday} г.р.'

    def get_absolute_url(self):
        return reverse('persons', kwargs={'research_id': self.research.primary_key})
