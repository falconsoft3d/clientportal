from django.urls import path
from .views import ApiView

urlpatterns = [
     path('products/<str:token>', ApiView.as_view(), name='api_products_list'),
     path('products/<str:token>/<int:id>', ApiView.as_view(), name='api_product')
]