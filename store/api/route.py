from rest_framework.routers import DefaultRouter
from store.api.views import ProductModeViewSet

router_product = DefaultRouter()

router_product.register(prefix='products', basename='products', viewset=ProductModeViewSet)