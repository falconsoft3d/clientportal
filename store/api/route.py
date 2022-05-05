from rest_framework.routers import DefaultRouter
from store.api.views import ProductModeViewSet, ColorModeViewSet, SizeModeViewSet

router_product = DefaultRouter()

router_product.register(prefix='products', basename='products', viewset=ProductModeViewSet)
router_product.register(prefix='colors', basename='colors', viewset=ColorModeViewSet)
router_product.register(prefix='sizes', basename='sizes', viewset=SizeModeViewSet)