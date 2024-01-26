from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('profile/', views.profile, name = 'profile'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
    path('change_password/', views.pass_change, name = 'change_password'),
    path('logout/', views.user_logout, name = 'logout'),
]
