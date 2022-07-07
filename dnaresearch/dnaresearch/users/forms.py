from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Адрес электронной почты',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control mb-2',
                'autofocus': True
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control mb-2'
            }
        ),
    )
