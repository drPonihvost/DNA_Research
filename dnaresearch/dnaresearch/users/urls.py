from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/update/', views.update_profile, name='update_profile'),
]
