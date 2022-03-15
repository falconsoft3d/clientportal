from django.urls import path
from . import views


urlpatterns = [
     path('', views.store, name="store"),
     path('category/<slug:category_slug>/', views.store, name='products_by_category'),
     path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
     path('search', views.search, name='search'),
     path('favorites/', views.store, name='favorites_products'),
     path('add_favorites/<int:id>', views.add_favorites, name='add_favorites'),
     path('delete_favorites/<int:id>', views.delete_favorites, name='delete_favorites'),
]