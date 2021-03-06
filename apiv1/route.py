from rest_framework.routers import DefaultRouter
from apiv1.views import ProductModeViewSet, ColorModeViewSet, SizeModeViewSet, CategoryModeViewSet, AccountModeViewSet,\
    AccountPriceModeViewSet, OrderModeViewSet

from django.urls import path

router_api = DefaultRouter()

router_api.register(prefix='products', basename='products', viewset=ProductModeViewSet)
router_api.register(prefix='colors', basename='colors', viewset=ColorModeViewSet)
router_api.register(prefix='sizes', basename='sizes', viewset=SizeModeViewSet)
router_api.register(prefix='categories', basename='categories', viewset=CategoryModeViewSet)
router_api.register(prefix='accounts', basename='accounts', viewset=AccountModeViewSet)
router_api.register(prefix='account-prices', basename='account-prices', viewset=AccountPriceModeViewSet)
router_api.register(prefix='orders', basename='orders', viewset=OrderModeViewSet)