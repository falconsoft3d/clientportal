from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('logout/', views.logout, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('my_tickets/', views.my_tickets, name='my_tickets'),
    path('new_ticket/', views.new_ticket, name='new_ticket'),
    path('delete_ticket/<int:id>', views.delete_ticket, name='delete_ticket'),
    path('my_orders/', views.my_orders, name='my_orders'),
]