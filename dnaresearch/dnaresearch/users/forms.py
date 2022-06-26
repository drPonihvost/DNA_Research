from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import Profile

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)
        field_classes = {"username": forms.EmailField}


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email',)
        field_classes = {"username": forms.EmailField}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'surname', 'name', 'patronymic', 'post', 'rank', 'phone', 'department',
            'division', 'address', 'office_phone'
            )


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

# class LoginForm(forms.Form):
#     email = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
