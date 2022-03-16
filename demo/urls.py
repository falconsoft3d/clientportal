from django.urls import path
from . import views

urlpatterns = [
    path('generate_demo_data/', views.generate_demo_data, name='generate_demo_data'),
]