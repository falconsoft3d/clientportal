"""clientportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apiv1.route import router_api
handler404 = "clientportal.views.page_not_found_view"


schema_view = get_schema_view(
   openapi.Info(
      title="ClientPortal API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mfalconsoft@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


urlpatterns = [
    path('secureadmin/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('politicadecookies/', views.politicadecookies, name="politicadecookies"),
    path('', views.home, name="home"),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('accounts.urls')),
    path('store/', include('store.urls')),
    path('contact/', views.contact, name="contact"),
    path('cart/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('demo/', include('demo.urls')),
    path('apiv1/', include(router_api.urls)),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
