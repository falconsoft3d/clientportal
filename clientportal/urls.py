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

from store.api.route import router_product
from category.api.route import router_categories


handler404 = "clientportal.views.page_not_found_view"


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

    path('api/', include('accounts.api.router')),
    path('api/', include(router_product.urls)),
    path('api/', include(router_categories.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
