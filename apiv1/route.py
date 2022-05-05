from rest_framework.routers import DefaultRouter
from apiv1.views import ProductModeViewSet, ColorModeViewSet, SizeModeViewSet

router_api = DefaultRouter()

router_api.register(prefix='products', basename='products', viewset=ProductModeViewSet)
router_api.register(prefix='colors', basename='colors', viewset=ColorModeViewSet)
router_api.register(prefix='sizes', basename='sizes', viewset=SizeModeViewSet)