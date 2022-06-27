from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from core.views import error_handling, ErrorHandling
from .forms import UserAuthenticationForm


class UserLogin(LoginView, ErrorHandling):
    template_name = 'users/registration/login.html'
    form_class = UserAuthenticationForm


class UserLogout(LogoutView, ErrorHandling):
    pass