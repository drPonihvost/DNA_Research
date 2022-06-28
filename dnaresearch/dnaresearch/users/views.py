from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from core.views import error_handling, ErrorHandlingMixin
from .forms import UserAuthenticationForm


class UserLogin(ErrorHandlingMixin, LoginView):
    template_name = 'users/registration/login.html'
    form_class = UserAuthenticationForm


class UserLogout(ErrorHandlingMixin, LogoutView):
    pass