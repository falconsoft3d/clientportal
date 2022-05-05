from rest_framework.routers import DefaultRouter
from category.api.views import CategoryModeViewSet

router_categories = DefaultRouter()

router_categories.register(prefix='categories', basename='categories', viewset=CategoryModeViewSet)