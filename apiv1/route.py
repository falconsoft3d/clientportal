from rest_framework.routers import DefaultRouter
from apiv1.views import ProductModeViewSet, ColorModeViewSet, SizeModeViewSet, CategoryModeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

router_api = DefaultRouter()

router_api.register(prefix='products', basename='products', viewset=ProductModeViewSet)
router_api.register(prefix='colors', basename='colors', viewset=ColorModeViewSet)
router_api.register(prefix='sizes', basename='sizes', viewset=SizeModeViewSet)
router_api.register(prefix='categories', basename='categories', viewset=CategoryModeViewSet)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]