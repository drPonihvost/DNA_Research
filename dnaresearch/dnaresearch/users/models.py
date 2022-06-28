from re import T
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


from .managers import CustomUserManager


class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_('administrator'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['pk']

    def __str__(self):
        return self.email


class Department(models.Model):
    """Модель для основного подразделения"""
    full_name = models.CharField(max_length=500, verbose_name='Полное наименование')
    abbreviated_name = models.CharField(max_length=100, verbose_name='Сокращенное наименование (для документов)')

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'
        ordering = ['pk']

    def __str__(self):
        return self.abbreviated_name


class Profile(models.Model):
    """Модель с данными профиля пользователя"""
    #  Всё поля относительно пользователя
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=30, verbose_name='Фамилия', null=True)
    name = models.CharField(max_length=30, verbose_name='Имя', null=True)
    patronymic = models.CharField(max_length=30, verbose_name='Отчество', null=True)
    post = models.CharField(max_length=50, verbose_name='Должность', null=True)
    rank = models.CharField(max_length=50, verbose_name='Сп. звание', null=True)
    phone = PhoneNumberField(verbose_name='Мобильный телефон', null=True, blank=True)
    can_sign = models.BooleanField(verbose_name='Право на подпись', default=False)

    #  Все поля относительно места работы/службы
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, verbose_name='Департамент', null=True)
    division = models.CharField(max_length=100, verbose_name='Подразделение', null=True, blank=True)
    address = models.TextField(max_length=500, verbose_name='Адрес', null=True)
    office_phone = PhoneNumberField(verbose_name='Рабочий телефон', null=True)
    post_index = models.CharField(max_length=6, null=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f"{self.surname} {str(self.name)[0].upper()}. {str(self.patronymic)[0].upper()}."
