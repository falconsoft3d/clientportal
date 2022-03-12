from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('logout/', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
]