from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from core.views import error_handling, ErrorHandling
from .forms import CustomUserCreationForm, ProfileForm, UserAuthenticationForm


class UserLogin(LoginView):
    template_name = 'users/registration/login.html'
    form_class = UserAuthenticationForm


class UserLogout(ErrorHandling, LogoutView):
    pass


@error_handling
def signup(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            profile_form = ProfileForm(request.POST, instance=user.profile)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                user.save()
                profile.save()
                return redirect('register')
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'users/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
@error_handling
def update_profile(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('register')
    else:
        user_form = CustomUserCreationForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })