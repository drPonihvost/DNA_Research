from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import EmailField

from .models import Profile

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)
        field_classes = {"username": EmailField}


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email',)
        field_classes = {"username": EmailField}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'surname', 'name', 'patronymic', 'post', 'rank', 'phone', 'department',
            'division', 'address', 'office_phone'
            )


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
